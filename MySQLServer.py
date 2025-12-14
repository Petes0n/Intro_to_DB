import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # CONNECT TO MYSQL SERVER
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # CREATE DATABASE (WILL NOT FAIL IF IT ALREADY EXISTS)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # CLOSE CURSOR AND CONNECTION
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
