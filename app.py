from flask import Flask, request, redirect, url_for, render_template, session, flash
import os
import base64
import time
#import BottleSensors as bs
#import Temp_sensor as tp
import json

app = Flask(__name__)
app.secret_key = 'FIAN23!de'

with open("bottle_count.json", "r") as file:
    data = json.load(file)
    value = int(data['count'])

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
            sensorSts = 12 #bs.bottle_counter()
            count = value
            temper = 5 #tp.TempCalc()
            templateData = {
                'temperature': temper,
                'title': 'GPIO input Status!',
                'button': sensorSts,
                'quantity': count,
            }
            return render_template("Mate_website.html", **templateData)
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


#def start() -> None:
 #   app.run(host="192.168.30.154", port="5010", debug=True)

if __name__ == "__main__":
    app.run()