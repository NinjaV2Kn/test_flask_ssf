from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
    """
    Web Page to Display Login Form and process form. 
    """
    if request.method == "POST":
        pw = os.environ.get('pass_api_key')
        if request.form['password'] == pw:
            return redirect(request.args.get("Mate_website.html") or "/")        

    return render_template("LoginDashboard.html")

if __name__ == "__main__":
    app.run(host='192.168.30.154', port=5010, debug=True)