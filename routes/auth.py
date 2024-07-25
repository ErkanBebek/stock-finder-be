# routes/users.py
from flask import Blueprint, request, jsonify
from models.auth import get_user_by_username,login_user,logout_user
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    user = get_user_by_username(username)
    print(f"User: {user}")
    
    if user and check_password_hash(user['password'], password):  # Adjusted to dictionary access
        login = login_user(user)
        print(f"login: {login}")
        return jsonify({
            "message": "Login successful",
            "id": login[id],
            "hash": login[hash],
            "phone": user["phone"],
            "name": user["name"],
            "surname": user["surname"],
            "email": user["email"],
            "role": user["role"],
        }), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    logout_user(data.id,data.hash)
    return jsonify({"message": "Logout successful"}), 200

