from flask import Flask, request, redirect, url_for, render_template, session, flash, jsonify
import os
import base64
import time
import json
from azure.iot.device import IoTHubDeviceClient

CONNECTION_STRING = "HostName=fian23-fridge-hub.azure-devices.net;DeviceId=Raspberry;SharedAccessKey=FnuqGxLtzbBQS1aQXgBE02dR5RTLyOxfhAIoTBgmTKU="

app = Flask(__name__)
app.secret_key = 'FIAN23!de'

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)




@app.route("/")
def index():
    return redirect(url_for('login'))

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

    def message_handler(message) -> int:
        print("started message_handler")
        # print data from both system and application (custom) properties
        temp = vars(message)['custom_properties']['temp']
        bottles = vars(message)['custom_properties']['bottles']
        count = vars(message)['custom_properties']['count']
        print("loaded props")
        with open("bottle_count.json", "w") as file:
            json.dump({"bottles": bottles, "temp": temp, "count": count}, file)
        print("dumped the message")

    try:
        client.on_message_received = message_handler
        print("loaded on_message_received")
        with open("bottle_count.json", "r") as file: #opens the json to get the data
            print("loaded json file")
            data = json.load(file)
            value = int(data['count'])
            bottles = int(data['bottles'])
            temperature = int(data['temp'])
            print("loaded data from json")


        if is_logged_in():
            sensorSts = bottles
            count = value
            temper = temperature
            templateData = {
                'temperature': temper,
                'title': 'GPIO input Status!',
                'button': sensorSts,
                'quantity': count,
            }
            print("loaded is_logged_in")
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
# def start() -> None:    
#     app.run(host="192.168.30.32", port="5010", debug=True)

if __name__ == "__main__":
    app.run()