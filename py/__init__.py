from flask import Flask
from flask_cors import CORS
from .auth.firebase_auth import init_firebase
from .core.database import init_db
import os

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Configurações
    app.config.from_pyfile('../config.py')
    
    # Inicializações
    init_firebase(app)
    init_db(app)
    
    # Blueprints
    from .routes import main_bp, auth_bp, api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app