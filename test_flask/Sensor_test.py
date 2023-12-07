from flask import Flask, render_template
import BottleSensors as bs
import os
import bottle_counter as gbc

app = Flask(__name__)

@app.route("/")
def index():
    sensorSts = bs.bottle_counter()
    count     = gbc.sold_bottle_count
    templateData = {
        'title': 'GPIO input Status!',
        'button': sensorSts,
        'quantity': count,
    
    }
                         #'Mate_website.html'
    return render_template('index.html', **templateData)

def startFlask():
    app.run(host='192.168.30.154', port=5000, debug=True)
