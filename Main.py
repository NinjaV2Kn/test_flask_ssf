import RPi.GPIO as GPIO
from nanoleafapi import Nanoleaf, NanoleafDigitalTwin
import time

nl = Nanoleaf("192.168.30.132") # setup nanoleaf
digital_twin = NanoleafDigitalTwin(nl) #setup nanoleaf digital twin(used to control each individuial nanoleaf)


# each sensor is a GPIO pin so it can be diffrent(in this case buttons where used).
sensor1 = 4 # bottle slot 1
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

def setup_GPIO():
    """setup the GPIO pins."""
    GPIO.setwarnings(False) #Disable warnings
    GPIO.setmode(GPIO.BCM) #Set GPIO pin numbering
    GPIO.setup(sensor1, GPIO.IN) #Sensor 1
    GPIO.setup(sensor2, GPIO.IN) #Sensor 2
    GPIO.setup(sensor3, GPIO.IN) #Sensor 3
    GPIO.setup(sensor4, GPIO.IN) #Sensor 4
    #GPIO.setup(sensor5, GPIO.IN) #Sensor 5
    #GPIO.setup(sensor6, GPIO.IN) #Sensor 6
    #GPIO.setup(sensor7, GPIO.IN) #Sensor 7
    #GPIO.setup(sensor8, GPIO.IN) #Sensor 8
    #GPIO.setup(sensor9, GPIO.IN) #Sensor 9
    #GPIO.setup(sensor10, GPIO.IN) #Sensor 10
    #GPIO.setup(sensor11, GPIO.IN) #Sensor 11
    #GPIO.setup(sensor12, GPIO.IN) #Sensor 12
    #GPIO.setup(sensor13, GPIO.IN) #Sensor 13
    #GPIO.setup(sensor14, GPIO.IN) #Sensor 14
    #GPIO.setup(sensor15, GPIO.IN) #Sensor 15
    #GPIO.setup(sensor16, GPIO.IN) #Sensor 16

def button_state(input_pin: int):
    """returns the state of the sensor so you know if it is occupied or empty."""
    if GPIO.input(input_pin): 
        return "occupied"
    else:
        return "empty"
    
def bottle_counter():
    """counts how many bottles are in the fridge."""
    all_sensors = [sensor1, sensor2, sensor3, sensor4] #, sensor5, sensor6, sensor7, sensor8, sensor9, sensor10, sensor11, sensor12, sensor13, sensor14, sensor15, sensor16]
    occupied_sensors = []

    for sensor in all_sensors:
        if button_state(sensor) == "occupied":
            if sensor not in occupied_sensors:
                occupied_sensors.append(sensor)
        else:
            if sensor in occupied_sensors:
                occupied_sensors.remove(sensor)
    return len(occupied_sensors)

def nanoleaf_indicator():
    """shows you on the nanoleafes how many bottles are in the fridge(only works with 16 sensors and with only 6 nanoleafes)."""

    # each nanoleaf panel has a diffrent id so you can control each panel individuialy.
    panel_middle_bottom = 55455
    panel_left_bottom = 27581
    panel_right_bottom = 41647
    panel_left_middle = 5517
    panel_right_middle = 1967
    panel_top = 54208

    if bottle_counter() == 16: # if all sensors are occupied all the panels will turn Green
        digital_twin.set_all_colors((0, 255, 0)) # set all panels to green
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 15: # if 15 sensors are occupied all the panels will turn Green and the top panel will turn orange
        digital_twin.set_all_colors((0, 255, 0))
        digital_twin.set_color(panel_top, (255, 100, 0)) # set the top panel to orange
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 14: # if 14 sensors are occupied all the panels will turn Green and the top panel and the left middle panel will turn orange
        digital_twin.set_all_colors((0, 255, 0))
        digital_twin.set_color(panel_top, (255, 100, 0))
        digital_twin.set_color(panel_left_middle, (255, 100, 0))
        digital_twin.sync()
        time.sleep(10)
        
    elif bottle_counter() == 13: # if 13 sensors are occupied all the panels will turn Green and the top panel, the left middle panel and the right middle panel will turn orange
        digital_twin.set_all_colors((0, 255, 0))
        digital_twin.set_color(panel_top, (255, 100, 0))
        digital_twin.set_color(panel_left_middle, (255, 100, 0))
        digital_twin.set_color(panel_right_middle, (255, 100, 0))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 12: # 
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_middle_bottom, (0, 255, 0))
        digital_twin.set_color(panel_right_bottom, (0, 255, 0))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 11:
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_right_bottom, (0, 255, 0))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 10: # if 10 sensors are occupied all the panels will turn orange
        digital_twin.set_all_colors(255, 100, 0)
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 9:
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_top, (255, 0, 0))
        digital_twin.sync()
        time.sleep(10)
    
    elif bottle_counter() == 8:
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_top, (255, 0, 0))
        digital_twin.set_color(panel_left_middle, (255, 0, 0))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 7:
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_top, (255, 0, 0))
        digital_twin.set_color(panel_left_middle, (255, 0, 0))
        digital_twin.set_color(panel_right_middle, (255, 0, 0))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 6:
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.set_color(panel_middle_bottom, (255, 100, 0))
        digital_twin.set_color(panel_right_bottom, (255, 100, 0))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 5:
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.set_color(panel_right_bottom, (255, 100, 0))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 4: # if 4 sensors are occupied all the panels will turn red
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 3:
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.set_color(panel_top, (255, 255, 255))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 2:
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.set_color(panel_top, (255, 255, 255))
        digital_twin.set_color(panel_left_middle, (255, 255, 255))
        digital_twin.set_color(panel_right_middle, (255, 255, 255))
        digital_twin.sync()
        time.sleep(10)

    elif bottle_counter() == 1:
        digital_twin.set_all_colors((255, 255, 255))
        digital_twin.set_color(panel_middle_bottom, (255, 0, 0))
        digital_twin.sync()
        time.sleep(10)
    
    elif bottle_counter() == 0: # if all sensors are empty all the panels will turn white
        digital_twin.set_all_colors((255, 255, 255))
        digital_twin.sync()
        time.sleep(10)


def main():
    """main function."""
    try:
        setup_GPIO()

        print("setup complete")
        print("press CTRL+C to exit")

        while True:
            bottle_counter()

            time.sleep(0.1)

            nanoleaf_indicator()

    except KeyboardInterrupt:
        GPIO.cleanup()

main()
