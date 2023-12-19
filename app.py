from flask import Flask, request, redirect, url_for, render_template, session, flash
import os
import base64
import time
import dataReceived as rd
import json

app = Flask(__name__)
app.secret_key = 'FIAN23!de'

with open("bottle_count.json", "r") as file:
    data = json.load(file)
    value = int(data['count'])

import time
from azure.iot.device import IoTHubDeviceClient

RECEIVED_MESSAGES = 0
bottles: int= 0

CONNECTION_STRING = "HostName=fian23-fridge-hub.azure-devices.net;DeviceId=Raspberry;SharedAccessKey=FnuqGxLtzbBQS1aQXgBE02dR5RTLyOxfhAIoTBgmTKU="

def message_handler(message):
    global RECEIVED_MESSAGES
    RECEIVED_MESSAGES += 1
    print("")
    print("Message received:")

    # print data from both system and application (custom) properties
    bottles = vars(message)['custom_properties']['BottleSensors']
    print(bottles)

    print("Total calls received: {}".format(RECEIVED_MESSAGES))

def mainMessage():
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

@app.route("/")
def index():
    return render_template("login.html")

# This function checks if the user is logged in
def is_logged_in():
    return 'logged_in' in session and session['logged_in']


# Route for the login page
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        password_attempt = request.form['password']

        if password_attempt == app.secret_key:
            session['logged_in'] = True
            return redirect(url_for('protected'))
        else:
            flash('Invalid password!', 'error')


    return render_template('login.html')


# Route for the protected page
@app.route('/Mate')
def protected():
    try:
        with open("bottle_count.json", "r") as file:
            data = json.load(file)
            value = int(data['count'])


        if is_logged_in():
            sensorSts = bottles
            count = value
            temper = 5 #tp.TempCalc()
            templateData = {
                'temperature': temper,
                'title': 'GPIO input Status!',
                'button': sensorSts,
                'quantity': count,
            }
            return render_template("probe.html", **templateData)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        print(e)
        return redirect(url_for('login'))

# Route for logging out
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

mainMessage()
#def start() -> None:
 #   app.run(host="192.168.30.154", port="5010", debug=True)

if __name__ == "__main__":
    app.run()