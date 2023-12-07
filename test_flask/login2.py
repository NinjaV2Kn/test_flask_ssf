from flask import Flask, request, redirect, url_for, render_template, session, flash
import os
import base64
import time

app = Flask(__name__)
app.secret_key = 'FIAN23!de'

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

        # Replace 'your_password' with the actual password you want to use
        if password_attempt == app.secret_key:
            session['logged_in'] = True
            return redirect(url_for('protected'))
        else:
            flash('Invalid password!', 'error')


    return render_template('login.html')


# Route for the protected page
@app.route('/protected')
def protected():
    if is_logged_in():
        return render_template('Mate_website.html')
    else:
        return redirect(url_for('login'))


# Route for logging out
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host="192.168.30.154", port="5010", debug=True)
