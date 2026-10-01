from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Configuración de Talisman
    talisman = Talisman(
        app,
        content_security_policy={
            'default-src': [
                "'self'"
            ],
            'style-src': [
                "'self'", 'https://fonts.googleapis.com'
            ],
            'font-src': [
                "'self'", 'https://fonts.gstatic.com'
            ]
        },
        force_https=True,          # Obliga HTTPS
        strict_transport_security=True,  # HSTS
        session
