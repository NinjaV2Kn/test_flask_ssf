import RPi.GPIO as GPIO
import time
import Nanoleaf as nls

# each sensor is a GPIO pin so it can be diffrent(in this case buttons where used).
sensor1 = 18 # bottle slot 1
sensor2 = 17 # bottle slot 2
sensor3 = 27 # bottle slot 3
sensor4 = 22 # bottle slot 4
#sensor5 = 5 # bottle slot 5
#sensor6 = 6 # bottle slot 6
#sensor7 = 13 # bottle slot 7
#sensor8 = 19 # bottle slot 8
#sensor9 = 26 # bottle slot 9
#sensor10 = 18 # bottle slot 10
#sensor11 = 23 # bottle slot 11
#sensor12 = 24 # bottle slot 12
#sensor13 = 25 # bottle slot 13
#sensor14 = 12 # bottle slot 14
#sensor15 = 16 # bottle slot 15
#sensor16 = 20 # bottle slot 16

all_sensors = [sensor1, sensor2, sensor3, sensor4] #, sensor5, sensor6, sensor7, sensor8, sensor9, sensor10, sensor11, sensor12, sensor13, sensor14, sensor15, sensor16]

def setup_GPIO() -> None:
    """setup the GPIO pins."""
    try:
        GPIO.setwarnings(False) #Disable warnings
        GPIO.setmode(GPIO.BCM) #Set GPIO pin numbering
        for sensor in all_sensors:
            GPIO.setup(sensor, GPIO.IN) #Setup GPIO as input
    except Exception as e:
        print(e)

def button_state(input_pin: int) -> bool:
    """returns the state of the sensor so you know if it is occupied or empty."""
    try:
        if GPIO.input(input_pin): 
            return True
        else:
            return False
    except Exception as e:
        print(e)
    
def bottle_counter() -> int:
    """counts how many bottles are in the fridge."""
    occupied_sensors = []
    try:
        for sensor in all_sensors:
            if button_state(sensor):
                if sensor not in occupied_sensors:
                    occupied_sensors.append(sensor)
            else:
                if sensor in occupied_sensors:
                    occupied_sensors.remove(sensor)
        return len(occupied_sensors)
    except Exception as e:
        print(e)