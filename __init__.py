from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Configuración de Talisman para seguridad
    talisman = Talisman(
        app,
        content_security_policy={
            'default-src': ["'self'"],
            'style-src': ["'self'", 'https://fonts.googleapis.com'],
            'font-src': ["'self'", 'https://fonts.gstatic.com'],
            'script-src': ["'self'"]
        },
        force_https=True,                 # Obliga a usar HTTPS
        strict_transport_security=True,   # Activa HSTS
        session_cookie_secure=True,       # Cookies solo por HTTPS
        session_cookie_http_only=True     # Cookies no accesibles vía JS
    )

    @app.route('/')
    def index():
        return "Aplicación segura con Talisman"

    return app
