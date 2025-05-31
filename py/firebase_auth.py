import firebase_admin
from firebase_admin import auth, credentials
from flask import current_app

def init_firebase(app):
    if not firebase_admin._apps:
        cred = credentials.Certificate(app.config['FIREBASE_CREDENTIALS'])
        firebase_admin.initialize_app(cred)

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        current_app.logger.error(f"Firebase auth error: {str(e)}")
        return None