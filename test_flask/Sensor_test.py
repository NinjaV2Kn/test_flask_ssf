from flask import Flask, render_template
import BottleSensors as bs

app = Flask(__name__)

@app.route("/")
def index():
    sensorSts = bs.bottle_counter()
    templateData = {
        'title': 'GPIO input Status!',
        'button': sensorSts,
    }
    
    return render_template('index.html', **templateData)

def startFlask():
    app.run(host='192.168.30.154', port=5000, debug=True)