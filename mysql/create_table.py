import mysql.connector
from mysql.connector import errorcode

# MySQL database configuration
config = {
    'user': 'diot',        # Replace with your MySQL username
    'password': 'Diot@1234',    # Replace with your MySQL password
    'host': 'localhost',            # Replace with your MySQL host if different
    'database': 'weather_db'        # Database name
}

try:
    # Connect to MySQL server
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    print("Connected to MySQL server.")

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS weather_db")
    print("Database 'weather_db' is ready.")

    # Use the specified database
    cursor.execute("USE weather_db")

    # SQL query to create the weather_data table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME NOT NULL,
        temperature FLOAT,
        humidity FLOAT,
        pressure FLOAT,
        wind_speed FLOAT,
        wind_direction FLOAT,
        precipitation FLOAT
    )
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    print("Table 'weather_data' is ready.")

except mysql.connector.Error as err:
    # Handle errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist and could not be created.")
    else:
        print(f"Error: {err}")
else:
    # Close the cursor and connection
    cursor.close()
    cnx.close()
    print("MySQL connection closed.")
