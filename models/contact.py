# models/users.py
from db import get_db_connection
from datetime import datetime

def get_all_messages_by_reciever_id(reciever_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    # query = "SELECT contact_message.*,users.username, users.email, users.name, users.surname FROM  contact_message JOIN users ON contact_message.reciever_id = users.ID WHERE reciever_id= %s ORDER BY  created_at DESC"
    query = "SELECT * FROM  contact_message  WHERE reciever_id= %s ORDER BY  created_at DESC"
    cursor.execute(query, (reciever_id,))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# def get_comments_by_slug(slug):
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     query = "SELECT stock_id, stock_locale, user_id, comment, created_at, updated_at FROM comments WHERE slug = %s"
#     cursor.execute(query, (slug,))
#     result = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return result

def add_message(user_id, reciever_id, message,name,email):
    connection = get_db_connection()
    cursor = connection.cursor()

    get_date = datetime.now()
    created_at = get_date.strftime('%Y-%m-%d %H:%M:%S')

    query = """
        INSERT INTO contact_message (user_id, reciever_id, message, created_at,name,email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, reciever_id, message, created_at,name,email))
    connection.commit()
    cursor.close()
    connection.close()
