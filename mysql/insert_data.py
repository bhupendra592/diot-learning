import mysql.connector
from mysql.connector import errorcode
import random
import time
from datetime import datetime

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

    # Function to insert random weather data
    def insert_random_weather_data():
        # Generate random data for each parameter
        timestamp = datetime.now()
        temperature = round(random.uniform(-30, 50), 2)       # Temperature in degrees Celsius
        humidity = round(random.uniform(0, 100), 2)           # Humidity in percentage
        pressure = round(random.uniform(950, 1050), 2)        # Atmospheric pressure in hPa
        wind_speed = round(random.uniform(0, 150), 2)         # Wind speed in km/h
        wind_direction = round(random.uniform(0, 360), 2)     # Wind direction in degrees
        precipitation = round(random.uniform(0, 200), 2)      # Precipitation in mm

        # SQL query to insert data into weather_data table
        insert_query = """
        INSERT INTO weather_data (timestamp, temperature, humidity, pressure, wind_speed, wind_direction, precipitation)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Data to insert
        data = (timestamp, temperature, humidity, pressure, wind_speed, wind_direction, precipitation)

        # Execute the query
        cursor.execute(insert_query, data)
        cnx.commit()
        print(f"Inserted data at {timestamp}.")

    # Infinite loop to insert data every 10 seconds
    try:
        while True:
            insert_random_weather_data()
            time.sleep(10)
    except KeyboardInterrupt:
        print("Data insertion stopped by user.")

except mysql.connector.Error as err:
    # Handle errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist.")
    else:
        print(f"Error: {err}")
finally:
    # Close the cursor and connection
    cursor.close()
    cnx.close()
    print("MySQL connection closed.")
