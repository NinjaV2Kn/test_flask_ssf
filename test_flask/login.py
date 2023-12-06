from flask import Flask, render_template, request, redirect
from flask_security.utils import hash_password as hash_pass
import os

app = Flask(__name__)

@app.route("/login/", methods=["GET", "POST"])
def login_page():
    """
    Web Page to Display Login Form and process form. 
    """
    if request.method == "POST":
        pw = os.environ.get('pass_api_key')
        #If we found a user based on username then compare that the submitted
        #password matches the password in the database.  The password is stored
        #is a slated hash format, so you must hash the password before comparing
        #it.
        if request.form['password'] == pw:
            return redirect(request.args.get("next") or "/")        

    return render_template("loginPage.html")

if __name__ == "__main__":
    app.run(host='192.168.30.154', port=5010, debug=True)