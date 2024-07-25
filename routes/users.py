# routes/users.py
from flask import Blueprint, request, jsonify
from models.users import get_all_users, add_user

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    added = add_user(data)
    print(added)
    return added
