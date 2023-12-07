from flask import Flask, render_template
import BottleSensors as bs
import os



with open("bottle_count.json", "r") as file:
    data = json.load(file)
    value = int(data['count'])

app = Flask(__name__)

@app.route("/")
def index():
    sensorSts = bs.bottle_counter()
    count     = value
    templateData = {
        'title': 'GPIO input Status!',
        'button': sensorSts,
        'quantity': count,
    
    }
                         #'Mate_website.html'
    return render_template('index.html', **templateData)

def startFlask():
    app.run(host='192.168.30.154', port=5000, debug=True)