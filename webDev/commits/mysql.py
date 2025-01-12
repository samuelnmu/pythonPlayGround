import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host="localhost",     # Replace with your MySQL server hostname or IP
            database="your_database",  # Replace with your database name
            user="your_username",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            print("Connection to MySQL established successfully!")
            
            # Retrieve and print server info
            db_info = connection.get_server_info()
            print("MySQL Server version:", db_info)
            
            # Create a cursor object and execute a query
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Connected to database:", record)
    
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Call the function
connect_to_mysql()
