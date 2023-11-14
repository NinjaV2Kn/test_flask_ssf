import RPi.GPIO as GPIO
import time
import Reader

class BottleSensor:
        
        def __init__(self, sensor: str, pin: int):
            self.sensor = sensor
            self.pin = pin
            self.reader = Reader(pin)

        def read(self):
            return self.reader.read()
            
        def getoutput(self):
            return self.sensor + ": " + str(self.read())

slot1 = BottleSensor("Slot 1", 4)
print(slot1.getoutput())
