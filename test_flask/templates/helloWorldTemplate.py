from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)  # Use __name__ instead of __SSF__

sensor1 = 21  # Define sensor1, replace 21 with your actual GPIO pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1, GPIO.IN)

@app.route('/')
def index():
   # Read Sensors Status
   sensorSts = GPIO.input(sensor1)

   templateData = {
      'title' : 'GPIO input Status!',
      'button'  : sensorSts,
   }
   return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='192.168.30.154', port=80, debug=True)