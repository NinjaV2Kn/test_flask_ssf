import RPi.GPIO as GPIO
import time

class Reader:
    
    def __init__(self, pin): # pin is the GPIO pin number
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def read(self): # returns the value of the pin
        return GPIO.input(self.pin)
