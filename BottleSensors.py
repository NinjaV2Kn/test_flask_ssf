import RPi.GPIO as GPIO
import time

sensor1 = 4
sensor2 = 17
sensor3 = 27
sensor4 = 22

GPIO.setmode(GPIO.BCM) #Set GPIO pin numbering
GPIO.setup(sensor1, GPIO.IN) #Sensor 1
GPIO.setup(sensor2, GPIO.IN) #Sensor 2
GPIO.setup(sensor3, GPIO.IN) #Sensor 3
GPIO.setup(sensor4, GPIO.IN) #Sensor 4

def button_state(input_pin: int): # returns the value of the pin
    if GPIO.input(input_pin): 
        return "occupied"
    else:
        return "slot empty"
    
while True:
    if button_state(sensor1) == "occupied":
        print("Sensor 1: Occupied")
        time.sleep(0.5)
    elif button_state(sensor2) == "occupied":
        print("Sensor 2: Occupied")
        time.sleep(0.5)
    elif button_state(sensor3) == "occupied":
        print("Sensor 3: Occupied")
        time.sleep(0.5)
    elif button_state(sensor4) == "occupied":
        print("Sensor 4: Occupied")
        time.sleep(0.5)
