#!/usr/bin/env python3
import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

"""
Sube la carpeta brain/ a Google Drive para que NotebookLM la indexe.

Uso:
  python scripts/sync_to_drive.py           # sube brain/ completo
  python scripts/sync_to_drive.py --dry-run # muestra qué subiría sin subir
  python scripts/sync_to_drive.py --list    # lista archivos existentes en Drive

Setup (una sola vez):
  1. Ve a https://console.cloud.google.com/
  2. Crea proyecto → Habilita "Google Drive API"
  3. Credenciales → OAuth 2.0 → Tipo: Aplicación de escritorio
  4. Descarga el JSON → guárdalo como credentials/client_secret.json
  5. En .env agrega: DRIVE_FOLDER_ID=id_de_tu_carpeta_en_drive
     (el ID está en la URL de Drive: drive.google.com/drive/folders/ESTE_ID)
  6. Primera vez: ejecuta este script → se abrirá el browser para autorizar
     El token se guarda en credentials/drive_token.json (no subir a git)

Requisitos:
  pip install google-api-python-client google-auth google-auth-oauthlib python-dotenv
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
except ImportError:
    print("Instala dependencias:")
    print("  pip install google-api-python-client google-auth google-auth-oauthlib python-dotenv")
    sys.exit(1)


ROOT = Path(__file__).parent.parent
BRAIN_DIR = ROOT / "brain"
CREDS_DIR = ROOT / "credentials"
CLIENT_SECRET = CREDS_DIR / "client_secret.json"
TOKEN_FILE = CREDS_DIR / "drive_token.json"

SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def load_config() -> str:
    load_dotenv(ROOT / ".env")
    folder_id = os.getenv("DRIVE_FOLDER_ID", "").strip()
    # Limpiar parámetros URL que se copian accidentalmente (ej: ?hl=es)
    folder_id = folder_id.split("?")[0].split("&")[0].rstrip("/")

    if not folder_id:
        print("ERROR: DRIVE_FOLDER_ID no encontrado en .env")
        print()
        print("Para encontrar el ID de tu carpeta de Drive:")
        print("  1. Abre la carpeta '🧠 Cerebro Rodrigo' en drive.google.com")
        print("  2. La URL sera: drive.google.com/drive/folders/ABC123...")
        print("  3. Copia ese ABC123... y ponlo en .env:")
        print("     DRIVE_FOLDER_ID=ABC123...")
        sys.exit(1)
    return folder_id


def get_credentials() -> Credentials:
    if not CLIENT_SECRET.exists():
        print(f"ERROR: No se encontró {CLIENT_SECRET}")
        print()
        print("Para crear las credenciales:")
        print("  1. Ve a https://console.cloud.google.com/")
        print("  2. Crea un proyecto (ej: 'cerebro-rodrigo')")
        print("  3. APIs y servicios → Habilitar APIs → busca 'Google Drive API' → Habilitar")
        print("  4. Credenciales → + Crear credenciales → ID de cliente de OAuth 2.0")
        print("  5. Tipo: Aplicación de escritorio → Crear")
        print("  6. Descarga el JSON → guárdalo como credentials/client_secret.json")
        sys.exit(1)

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
            creds = flow.run_local_server(port=0)
        CREDS_DIR.mkdir(exist_ok=True)
        TOKEN_FILE.write_text(creds.to_json())
        print(f"✅ Token guardado en {TOKEN_FILE}")

    return creds


def get_or_create_subfolder(service, parent_id: str, folder_name: str) -> str:
    """Devuelve el ID de una subcarpeta, creándola si no existe."""
    query = (
        f"name='{folder_name}' and "
        f"'{parent_id}' in parents and "
        f"mimeType='application/vnd.google-apps.folder' and "
        f"trashed=false"
    )
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get("files", [])

    if items:
        return items[0]["id"]

    meta = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id],
    }
    folder = service.files().create(body=meta, fields="id").execute()
    return folder["id"]


def get_existing_file_id(service, folder_id: str, filename: str) -> str | None:
    query = f"name='{filename}' and '{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get("files", [])
    return items[0]["id"] if items else None


def upload_file(service, local_path: Path, folder_id: str, dry_run: bool = False) -> None:
    filename = local_path.name
    existing_id = get_existing_file_id(service, folder_id, filename)

    if dry_run:
        action = "actualizar" if existing_id else "subir"
        print(f"  [dry-run] {action}: {local_path.relative_to(ROOT)}")
        return

    media = MediaFileUpload(str(local_path), mimetype="text/markdown")

    if existing_id:
        service.files().update(fileId=existing_id, media_body=media).execute()
        print(f"  ↺ actualizado: {local_path.name}")
    else:
        meta = {"name": filename, "parents": [folder_id]}
        service.files().create(body=meta, media_body=media, fields="id").execute()
        print(f"  ↑ subido:     {local_path.name}")


def sync_brain(service, root_folder_id: str, dry_run: bool = False) -> None:
    folder_order = [
        "01-Proyectos",
        "02-Aprendizajes",
        "03-Tecnologias",
        "04-Ideas",
        "05-Metas",
        "06-Posts-Publicados",
    ]

    total = 0
    for folder_name in folder_order:
        local_folder = BRAIN_DIR / folder_name
        if not local_folder.exists():
            continue

        md_files = list(local_folder.glob("*.md"))
        if not md_files:
            continue

        print(f"\n📁 {folder_name}/")

        if not dry_run:
            drive_folder_id = get_or_create_subfolder(service, root_folder_id, folder_name)
        else:
            drive_folder_id = "dry-run-id"

        for md_file in sorted(md_files):
            upload_file(service, md_file, drive_folder_id, dry_run=dry_run)
            total += 1

    print(f"\n{'[dry-run] ' if dry_run else ''}✅ {total} archivos procesados")


def list_drive_files(service, folder_id: str) -> None:
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields="files(id, name, modifiedTime)",
        orderBy="name",
    ).execute()
    items = results.get("files", [])
    if not items:
        print("(Carpeta vacía)")
        return
    for item in items:
        print(f"  {item['name']}  [{item['id']}]  {item.get('modifiedTime', '')[:10]}")


def main():
    parser = argparse.ArgumentParser(
        description="Sincroniza brain/ con Google Drive para NotebookLM"
    )
    parser.add_argument("--dry-run", action="store_true", help="Muestra qué subiría sin subir")
    parser.add_argument("--list", action="store_true", help="Lista archivos en la carpeta Drive")
    args = parser.parse_args()

    folder_id = load_config()
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    if args.list:
        print(f"Archivos en Drive (carpeta ID: {folder_id}):\n")
        list_drive_files(service, folder_id)
        return

    print("🧠 Sincronizando brain/ → Google Drive\n")
    sync_brain(service, folder_id, dry_run=args.dry_run)

    if not args.dry_run:
        print()
        print("🔄 NotebookLM indexará los cambios automáticamente en ~5 minutos")
        print("   Verifica en: https://notebooklm.google.com/")


if __name__ == "__main__":
    main()
