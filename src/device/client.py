import time
import random
from azure.iot.device import IoTHubDeviceClient

# Replace these with your own values
CONNECTION_STRING = "<your IoT hub connection string>"
DEVICE_ID = "<your device id>"

# Create a client object
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# This function is called to send a message to the IoT hub
def send_message():
    # Generate a random message
    message = {"temperature": random.random() * 100}
    print("Sending message: {}".format(message))
    # Send the message
    client.send_message(message)

# Main loop
while True:
    # Send messages at a rate of 200 per second
    for i in range(200):
        send_message()
    # Sleep for 1 second
    time.sleep(1)
