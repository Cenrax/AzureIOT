import threading
import time
import azure.iot.device

# Set up the connection to Azure IoT Hub
connection_string = "YOUR_CONNECTION_STRING"
device_client = azure.iot.device.IoTHubDeviceClient.create_from_connection_string(connection_string)

# Define a function that will be executed in a separate thread
# for each of the concurrent requests
def send_message_to_iot_hub(thread_name):
    # Build the message to be sent to Azure IoT Hub
    message = {"timestamp": time.time(), "thread_name": thread_name}
    # Send the message to Azure IoT Hub
    device_client.send_message(message)

# Create a list of threads, one for each of the concurrent requests
threads = []
for i in range(100):
    thread_name = "thread-{}".format(i+1)
    thread = threading.Thread(target=send_message_to_iot_hub, args=(thread_name,))
    threads.append(thread)

# Start all the threads
for thread in threads:
    thread.start()

# Wait for all the threads to finish
for thread in threads:
    thread.join()

# Close the connection to Azure IoT Hub
device_client.disconnect()
