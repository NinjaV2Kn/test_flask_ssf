import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__SSF__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sensor = 4

sensorSts = GPIO.LOW

   # Set button and PIR sensor pins as an input
GPIO.setup(sensor1, GPIO.IN)   

	
@app.route("/")
def index():
	# Read Sensors Status
	sensorSts = GPIO.input(sensor)

	templateData = {
      'title' : 'GPIO input Status!',
      'button'  : sensorSts,

      }
   return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='192.168.30.154', port=80, debug=True)