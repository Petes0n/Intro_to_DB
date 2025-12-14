import mysql.connector

def create_database():
    connection = None
    try:
        # CONNECT TO MYSQL SERVER
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )

        cursor = connection.cursor()

        # CREATE DATABASE (DOES NOT FAIL IF IT EXISTS)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # HANDLE CONNECTION ERRORS
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # CLOSE CURSOR AND CONNECTION
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
