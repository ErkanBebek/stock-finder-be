# models/users.py
from db import get_db_connection
from datetime import datetime
import mysql.connector

# get_watch_list_by_userID,
#     delete_watched_by_stocksID,
#     add_watch_list

def get_watch_list_by_userID(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM watch_list WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def add_watch_list(data):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        get_date = datetime.now()
        created_at = get_date.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            """INSERT INTO watch_list (stock_symbol, stock_locale, user_id, watched_price, watch_date) 
               VALUES (%s, %s, %s, %s, %s)""",
            (
                data['stock_symbol'],
                data['stock_locale'],
                data['user_id'],
                data['watched_price'],
                created_at
            )
        )
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Watch list item added successfully"}
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {"message": "Failed to add watch list item", "error": str(err)}


def delete_watched_by_stocksID(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM watch_list WHERE stock_symbol = %s AND stock_locale = %s"
    cursor.execute(query, (data["stock_symbol"],data["stock_locale"],))
    connection.commit()
    cursor.close()
    connection.close()
