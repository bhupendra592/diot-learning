import paho.mqtt.client as mqtt
import random
import time
import json

# MQTT broker details
broker = 'demo.thingsboard.io'
port = 1883
topic = 'v1/devices/me/telemetry'
username = 'aayushi'
password = ''  # Add password if required

# Create a new MQTT client instance
client = mqtt.Client()

# Set username and password
client.username_pw_set(username, password)

# Define callback functions (optional)
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
    else:
        print(f'Connection failed with code {rc}')

def on_publish(client, userdata, mid):
    print('Message published')

def on_disconnect(client, userdata, rc):
    print('Disconnected')

# Assign callback functions
client.on_connect = on_connect
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Connect to the broker
client.connect(broker, port, keepalive=60)

# Start the network loop in a separate thread
client.loop_start()

try:
    while True:
        # Generate random temperature and humidity values
        temperature = round(random.uniform(0.0, 50.0), 2)  # Temperature between 20.0 and 30.0
        humidity = round(random.uniform(30.0, 70.0), 2)     # Humidity between 30.0% and 70.0%

        # Create the payload
        payload = {
            "temperature": temperature,
            "humidity": humidity
        }

        # Convert the payload to a JSON formatted string
        payload_str = json.dumps(payload)

        # Publish the message
        result = client.publish(topic, payload_str, qos=1)
        status = result[0]

        if status == 0:
            print(f"Sent `{payload_str}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

        # Wait for 5 seconds before sending the next reading
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Stop the network loop and disconnect
    client.loop_stop()
    client.disconnect()
