# models/users.py
from flask import Blueprint, request, jsonify
from db import get_db_connection
from werkzeug.security import generate_password_hash
import uuid

def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_user_by_username(username):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT username FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return True if result else False

def get_user_by_email(email):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT email FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return True if result else False

def add_user(data):
    connection = get_db_connection()
    cursor = connection.cursor()

    if get_user_by_username(data['username']):
        return jsonify({'error': 'Kullanıcı adı zaten mevcut'}), 400

    if get_user_by_email(data['email']):
        return jsonify({'error': 'E-posta zaten mevcut'}), 400

    # Şifreyi hash'le
    hashed_password = generate_password_hash(data['password'])
    random_hash = str(uuid.uuid4())
    #HERKES AYNI ROL İLE BAŞLAR KULANICI OLARAK
    role=0
    cursor.execute(
        "INSERT INTO users (username, password, email, role, name, surname, phone, hash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (data['username'], hashed_password, data['email'], role, data['name'], data['surname'], data['phone'], random_hash)
    )
    connection.commit()
    cursor.close()
    connection.close()

    recorded = {
        "username": data['username'],
        "email": data['email'],
        "name": data['name'],
        "surname": data['surname'],
        "role": role,
        "phone": data['phone'],
        "password": hashed_password,
    }
    return jsonify({'message': 'User added successfully'}), 201