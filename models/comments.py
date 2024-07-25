# models/users.py
from db import get_db_connection
from datetime import datetime

def get_comments_by_stock_symbol(stock_symbol,locale):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM comments WHERE stock_symbol = %s AND stock_locale = %s"

    cursor.execute(query, (stock_symbol,locale))
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

def add_comment(data):
    connection = get_db_connection()
    cursor = connection.cursor()

    get_date = datetime.now()
    created_at = get_date.strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute(
        "INSERT INTO comments (stock_symbol, stock_locale, user_id, comment, created_at, updated_at) VALUES ( %s, %s, %s, %s, %s,%s)",
        (data['stock_symbol'], data['stock_locale'], data['user_id'], data['comment'], created_at, created_at)
    )
    connection.commit()
    cursor.close()
    connection.close()


def delete_comment_byID(comment_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM comments WHERE id = %s"
    cursor.execute(query, (comment_id,))
    connection.commit()
    cursor.close()
    connection.close()
