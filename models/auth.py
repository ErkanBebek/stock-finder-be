# models/users.py
from flask import Blueprint, request, jsonify
from db import get_db_connection
from datetime import datetime
import uuid

def get_user_by_username(username):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def login_user(user):
    generated_hash = str(uuid.uuid4())

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "UPDATE users SET hash = %s WHERE ID = %s"
    cursor.execute(query, (generated_hash,user['ID'],))
    connection.commit()  # Commit the transaction to save the update
    cursor.close()
    connection.close()
    return {id:user['ID'],hash:generated_hash}

def logout_user(user_id,user_hash):
    return "logout:" + user_id

