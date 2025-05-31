from flask import Blueprint, redirect, url_for
from flask_login import LoginManager, login_user
from werkzeug.security import generate_password_hash
import firebase_admin
from firebase_admin import auth

auth_bp = Blueprint('auth', __name__)

# Configura Firebase
cred = firebase_admin.credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)

@auth_bp.route('/login', methods=['POST'])
def login():
    id_token = request.json.get('token')
    try:
        decoded_token = auth.verify_id_token(id_token)
        user = User.get_or_create(decoded_token['uid'])
        login_user(user)
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 401