import RPi.GPIO as GPIO
import time

sensor1 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1, GPIO.IN) #Sensor 1

def button_state(input_pin: int):
    if GPIO.input(input_pin):
        return "occupied"
    else:
        return "slot empty"
    
while True:
    print(button_state(sensor1))
    time.sleep(0.5)
