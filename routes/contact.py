# routes/users.py
from flask import Blueprint, request, jsonify
from models.contact import (
    get_all_messages_by_reciever_id,
    add_message
    )

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/messages/reciever/<int:reciever_id>', methods=['GET'])
def get_message_by_recieverID(reciever_id):
    messages = get_all_messages_by_reciever_id(reciever_id)

    return jsonify(messages)

@contact_bp.route('/message', methods=['POST'])
def create_message():
    data = request.get_json()
    user_id = data.get('user_id')
    reciever_id = data.get('reciever_id')
    message = data.get('message')
    name = data.get('name')
    email = data.get('email')

    if not user_id or not reciever_id or not message:
        return jsonify({"error": "Missing data"}), 400


    add_message(user_id, reciever_id, message,name,email)
    return jsonify({"message": "Message added successfully"}), 201
