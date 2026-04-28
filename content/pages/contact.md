Title: Contacto
Slug: contact
Sortorder: 4
Status: published

<style>
.contact-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 48px 20px;
    margin-bottom: 40px;
    color: white;
    text-align: center;
    border-radius: 12px;
}
.contact-title { font-size: 2.6em; font-weight: 300; margin-bottom: 16px; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }
.contact-subtitle { font-size: 1.1em; opacity: .9; line-height: 1.6; max-width: 560px; margin: 0 auto; }

.contact-methods {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 24px;
    margin: 40px 0;
}
.contact-method {
    background: var(--pico-card-background-color);
    padding: 28px 24px;
    border-radius: 12px;
    border: 1px solid var(--pico-muted-border-color);
    text-align: center;
    transition: border-color .2s, transform .2s;
}
.contact-method:hover { border-color: #667eea; transform: translateY(-3px); }
.contact-icon { font-size: 2.5em; display: block; margin-bottom: 14px; }
.contact-method h3 { margin: 0 0 10px; font-size: 1.1em; }
.contact-method p { color: var(--pico-muted-color); font-size: .9em; margin-bottom: 18px; line-height: 1.5; }
.contact-link {
    display: inline-block;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white !important;
    padding: 10px 22px;
    text-decoration: none;
    border-radius: 25px;
    font-size: .9em;
    font-weight: 500;
    transition: opacity .2s;
}
.contact-link:hover { opacity: .85; }

.form-section {
    background: var(--pico-card-background-color);
    padding: 36px;
    border-radius: 12px;
    border: 1px solid var(--pico-muted-border-color);
    max-width: 580px;
    margin: 0 auto 40px;
}
.form-section h2 { text-align: center; margin-bottom: 28px; font-size: 1.6em; font-weight: 300; }
.form-group { margin-bottom: 20px; }
.form-group label { display: block; margin-bottom: 6px; font-weight: 500; font-size: .95em; }
.form-control {
    width: 100%; padding: 12px 14px;
    border: 1px solid var(--pico-muted-border-color);
    border-radius: 8px; font-size: 1em;
    background: var(--pico-background-color);
    color: var(--pico-color);
    box-sizing: border-box; transition: border-color .2s;
}
.form-control:focus { outline: none; border-color: #667eea; box-shadow: 0 0 0 3px rgba(102,126,234,.15); }
textarea.form-control { resize: vertical; min-height: 110px; }
.btn-submit {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white; padding: 13px 36px; border: none;
    border-radius: 25px; font-size: 1em; font-weight: 500;
    cursor: pointer; display: block; margin: 24px auto 0;
    min-width: 180px; transition: opacity .2s;
}
.btn-submit:hover { opacity: .88; }
@media(max-width:600px){
    .contact-title{font-size:2em;}
    .contact-methods{grid-template-columns:1fr;}
    .form-section{padding:24px 18px;}
}
</style>

<div class="contact-header">
  <h1 class="contact-title">¡Hablemos!</h1>
  <p class="contact-subtitle">
    Si tienes una consulta, una oportunidad de colaboración o simplemente quieres conectar,
    aquí tienes todas las formas de contactarme.
  </p>
</div>

<div class="contact-methods">
  <div class="contact-method">
    <span class="contact-icon">📧</span>
    <h3>Email Directo</h3>
    <p>Para consultas profesionales, oportunidades laborales o colaboraciones técnicas.</p>
    <a href="mailto:rorocabezas@gmail.com" class="contact-link">rorocabezas@gmail.com</a>
  </div>
  <div class="contact-method">
    <span class="contact-icon">💼</span>
    <h3>LinkedIn</h3>
    <p>Conectemos profesionalmente. Comparto insights sobre Data Science y Control de Gestión.</p>
    <a href="https://www.linkedin.com/in/rodrigo-cabezas-zu%C3%B1iga-698a8532/" class="contact-link" target="_blank">Conectar</a>
  </div>
  <div class="contact-method">
    <span class="contact-icon">💻</span>
    <h3>GitHub</h3>
    <p>Revisa mis proyectos de código abierto, contribuciones y desarrollos técnicos.</p>
    <a href="https://github.com/rodrigocabezasz" class="contact-link" target="_blank">Ver repos</a>
  </div>
  <div class="contact-method">
    <span class="contact-icon">📱</span>
    <h3>Teléfono</h3>
    <p>Para conversaciones directas sobre oportunidades urgentes.</p>
    <a href="tel:+56990202757" class="contact-link">+569 9020 2757</a>
  </div>
</div>

<div class="form-section">
  <h2>Envíame un Mensaje</h2>
  <form action="https://formspree.io/f/xjkodeed" method="POST">
    <div class="form-group">
      <label for="name">Tu Nombre</label>
      <input type="text" id="name" name="name" class="form-control" placeholder="¿Cómo te llamas?" required>
    </div>
    <div class="form-group">
      <label for="email">Tu Email</label>
      <input type="email" id="email" name="email" class="form-control" placeholder="tu.email@ejemplo.com" required>
    </div>
    <div class="form-group">
      <label for="subject">Asunto</label>
      <input type="text" id="subject" name="subject" class="form-control" placeholder="¿De qué quieres hablar?">
    </div>
    <div class="form-group">
      <label for="message">Mensaje</label>
      <textarea id="message" name="message" class="form-control" rows="5"
        placeholder="Cuéntame más detalles..." required></textarea>
    </div>
    <button type="submit" class="btn-submit">📤 Enviar Mensaje</button>
  </form>
</div>
