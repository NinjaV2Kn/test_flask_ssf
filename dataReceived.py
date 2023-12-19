import time
from azure.iot.device import IoTHubDeviceClient
import json
import app as app

bottles: int= 0

CONNECTION_STRING = "HostName=fian23-fridge-hub.azure-devices.net;DeviceId=Raspberry;SharedAccessKey=FnuqGxLtzbBQS1aQXgBE02dR5RTLyOxfhAIoTBgmTKU="

def message_handler(message) -> int:
    # print data from both system and application (custom) properties
    bottles = vars(message)['custom_properties']['BottleSensors']
    print(bottles)
    with open("bottle_count.json", "w") as file:
        json.dump({"bottles": bottles}, file)

def main():
    print ("Starting the Python IoT Hub C2D Messaging device sample...")

    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print ("Waiting for C2D messages, press Ctrl-C to exit")
    try:
        # Attach the handler to the client
        client.on_message_received = message_handler

        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()

if __name__ == '__main__':
    main()
    app.run