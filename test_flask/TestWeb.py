from flask import Flask, render_template
import BottleSensors as bs

app = Flask(__name__)

@app.route("/")
def index() -> None:
    sensors = 10
    templateData = {
        'button': bs.bottle_counter()
    }

    return render_template('Mate_website.html', **templateData)

def startFlask() -> None:
    app.run(host='192.168.30.154', port=5020, debug=True)