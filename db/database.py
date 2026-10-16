import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return connection

def get_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        query = "SELECT id, username, email, role FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        connection.close()


def insert_user(username, email, role):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
            INSERT INTO users (username, email, role)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (username, email, role))
        connection.commit()

        user_id = cursor.lastrowid

        return user_id

    finally:
        cursor.close()
        connection.close()

def delete_user_by_id(user_id):

    connection = get_connection()

    cursor = connection.cursor()

    try:
        query = "DELETE FROM users WHERE id = %s"

        cursor.execute(query, (user_id,))

        connection.commit()

    finally:
        cursor.close()
        connection.close()
