Title: Contacto
Date: 2025-08-24
Category: contacto
Tags: contacto
Slug: contacto

<style>
.contact-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 60px 20px;
    margin: -20px -20px 40px -20px;
    color: white;
    text-align: center;
    position: relative;
    border-radius: 0 0 20px 20px;
}

.contact-container {
    max-width: 800px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}

.contact-title {
    font-size: 3em;
    font-weight: 300;
    margin-bottom: 20px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.contact-subtitle {
    font-size: 1.2em;
    opacity: 0.9;
    margin-bottom: 30px;
    line-height: 1.6;
}

.contact-methods {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    margin: 40px 0;
    padding: 0 20px;
}

.contact-method {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.contact-method:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.contact-icon {
    font-size: 3em;
    margin-bottom: 20px;
    display: block;
}

.contact-method h3 {
    color: #333;
    margin-bottom: 15px;
    font-size: 1.3em;
}

.contact-method p {
    color: #666;
    margin-bottom: 20px;
    line-height: 1.6;
}

.contact-link {
    display: inline-block;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 12px 25px;
    text-decoration: none;
    border-radius: 25px;
    font-weight: 500;
    transition: all 0.3s ease;
}

.contact-link:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.form-section {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    margin: 40px 20px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.form-section h2 {
    text-align: center;
    color: #333;
    margin-bottom: 30px;
    font-size: 2em;
    font-weight: 300;
}

.form-group {
    margin-bottom: 25px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    color: #555;
    font-weight: 500;
    font-size: 1.1em;
}

.form-control {
    width: 100%;
    padding: 15px;
    border: 2px solid #e1e5e9;
    border-radius: 10px;
    font-size: 1em;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    box-sizing: border-box;
}

.form-control:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-control::placeholder {
    color: #aaa;
}

textarea.form-control {
    resize: vertical;
    min-height: 120px;
}

.btn-submit {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px 40px;
    border: none;
    border-radius: 25px;
    font-size: 1.1em;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    display: block;
    margin: 30px auto 0;
    min-width: 200px;
}

.btn-submit:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.decorative-element {
    position: absolute;
    border: 2px solid rgba(255,255,255,0.1);
    border-radius: 50%;
    z-index: 1;
}

.decorative-1 { top: 20px; right: 20px; width: 80px; height: 80px; }
.decorative-2 { bottom: 20px; left: 20px; width: 60px; height: 60px; }
.decorative-3 { top: 50%; right: 10%; width: 40px; height: 40px; }

@media (max-width: 768px) {
    .contact-title { font-size: 2.2em; }
    .contact-subtitle { font-size: 1.1em; }
    .contact-methods { grid-template-columns: 1fr; gap: 20px; }
    .form-section { margin: 20px 10px; padding: 30px 20px; }
    .contact-method { padding: 25px 20px; }
}
</style>

<div class="contact-header">
    <div class="contact-container">
        <h1 class="contact-title">¡Hablemos!</h1>
        <p class="contact-subtitle">
            Estaré encantado de conectar contigo. Si tienes alguna pregunta, una oportunidad de colaboración 
            o simplemente quieres saludar, aquí tienes todas las formas de contactarme.
        </p>
    </div>
    <div class="decorative-element decorative-1"></div>
    <div class="decorative-element decorative-2"></div>
    <div class="decorative-element decorative-3"></div>
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
        <a href="https://www.linkedin.com/in/rodrigocabezasz/" class="contact-link" target="_blank">Conectar en LinkedIn</a>
    </div>

    <div class="contact-method">
        <span class="contact-icon">💻</span>
        <h3>GitHub</h3>
        <p>Revisa mis proyectos de código abierto, contribuciones y desarrollos técnicos.</p>
        <a href="https://github.com/rodrigocabezasz" class="contact-link" target="_blank">Ver Repositorios</a>
    </div>

    <div class="contact-method">
        <span class="contact-icon">📱</span>
        <h3>Teléfono</h3>
        <p>Para conversaciones directas sobre oportunidades urgentes o consultas inmediatas.</p>
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
            <textarea id="message" name="message" class="form-control" rows="5" placeholder="Cuéntame más detalles sobre tu consulta, proyecto o propuesta..." required></textarea>
        </div>
        
        <button type="submit" class="btn-submit">
            📤 Enviar Mensaje
        </button>
    </form>
</div>

---

<div style="text-align: center; padding: 40px 20px; background: #f8f9fa; margin: 40px -20px -20px -20px; border-radius: 20px 20px 0 0;">
    <h3 style="color: #333; margin-bottom: 20px;">¿Prefieres una respuesta rápida?</h3>
    <p style="color: #666; margin-bottom: 25px;">
        Para consultas urgentes o conversaciones inmediatas, no dudes en contactarme directamente:
    </p>
    <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <a href="mailto:rorocabezas@gmail.com" style="background: #667eea; color: white; padding: 12px 25px; text-decoration: none; border-radius: 25px; font-weight: 500;">
            ✉️ Email Inmediato
        </a>
        <a href="https://www.linkedin.com/in/rodrigocabezasz/" style="background: #0a66c2; color: white; padding: 12px 25px; text-decoration: none; border-radius: 25px; font-weight: 500;" target="_blank">
            💬 Mensaje LinkedIn
        </a>
    </div>
</div>
