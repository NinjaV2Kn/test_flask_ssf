import time
import BottleSensors as bs
from nanoleafapi import Nanoleaf, NanoleafDigitalTwin

nl = Nanoleaf("192.168.30.132") # setup nanoleaf
digital_twin = NanoleafDigitalTwin(nl) #setup nanoleaf digital twin(used to control each individuial nanoleaf)

def nanoleaf_indicator():
    """shows you on the nanoleafes how many bottles are in the fridge(only works with 16 sensors and with only 6 nanoleafes)."""

    # each nanoleaf panel has a diffrent id so you can control each panel individuialy.
    panel_middle_bottom = 55455
    panel_left_bottom = 27581
    panel_right_bottom = 41647
    panel_left_middle = 5517
    panel_right_middle = 1967
    panel_top = 54208

    if bs.bottle_counter() == 16: # if all sensors are occupied all the panels will turn Green
        bs.digital_twin.set_all_colors((0, 255, 0)) # set all panels to green
        bs.digital_twin.sync() # sync the nanoleafes to set the colors
        time.sleep(10) # wait 10 seconds to not overload the nanoleafes

    elif bs.bottle_counter() == 15: # if 15 sensors are occupied all the panels will turn Green and the top panel will turn orange
        bs.digital_twin.set_all_colors((0, 255, 0))
        bs.digital_twin.set_color(panel_top, (255, 100, 0)) # set the top panel to orange
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 14: # if 14 sensors are occupied all the panels will turn Green and the top panel and the left middle panel will turn orange
        bs.digital_twin.set_all_colors((0, 255, 0))
        bs.digital_twin.set_color(panel_top, (255, 100, 0))
        bs.digital_twin.set_color(panel_left_middle, (255, 100, 0))
        bs.digital_twin.sync()
        time.sleep(10)
        
    elif bs.bottle_counter() == 13: # if 13 sensors are occupied all the panels will turn Green and the top panel, the left middle panel and the right middle panel will turn orange
        bs.digital_twin.set_all_colors((0, 255, 0))
        bs.digital_twin.set_color(panel_top, (255, 100, 0))
        bs.digital_twin.set_color(panel_left_middle, (255, 100, 0))
        bs.digital_twin.set_color(panel_right_middle, (255, 100, 0))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 12: # 
        bs.digital_twin.set_all_colors((255, 100, 0))
        bs.digital_twin.set_color(panel_middle_bottom, (0, 255, 0))
        bs.digital_twin.set_color(panel_right_bottom, (0, 255, 0))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 11:
        bs.digital_twin.set_all_colors((255, 100, 0))
        bs.digital_twin.set_color(panel_right_bottom, (0, 255, 0))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 10: # if 10 sensors are occupied all the panels will turn orange
        bs.digital_twin.set_all_colors(255, 100, 0)
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 9:
        bs.digital_twin.set_all_colors((255, 100, 0))
        bs.digital_twin.set_color(panel_top, (255, 0, 0))
        bs.digital_twin.sync()
        time.sleep(10)
    
    elif bs.bottle_counter() == 8:
        bs.digital_twin.set_all_colors((255, 100, 0))
        bs.digital_twin.set_color(panel_top, (255, 0, 0))
        bs.digital_twin.set_color(panel_left_middle, (255, 0, 0))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 7:
        bs.digital_twin.set_all_colors((255, 100, 0))
        bs.digital_twin.set_color(panel_top, (255, 0, 0))
        bs.digital_twin.set_color(panel_left_middle, (255, 0, 0))
        bs.digital_twin.set_color(panel_right_middle, (255, 0, 0))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 6:
        bs.digital_twin.set_all_colors((255, 0, 0))
        bs.digital_twin.set_color(panel_middle_bottom, (255, 100, 0))
        bs.digital_twin.set_color(panel_right_bottom, (255, 100, 0))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 5:
        bs.digital_twin.set_all_colors((255, 0, 0))
        bs.digital_twin.set_color(panel_right_bottom, (255, 100, 0))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 4: # if 4 sensors are occupied all the panels will turn red
        bs.digital_twin.set_all_colors((255, 0, 0))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 3:
        bs.digital_twin.set_all_colors((255, 0, 0))
        bs.digital_twin.set_color(panel_top, (255, 255, 255))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 2:
        bs.digital_twin.set_all_colors((255, 0, 0))
        bs.digital_twin.set_color(panel_top, (255, 255, 255))
        bs.digital_twin.set_color(panel_left_middle, (255, 255, 255))
        bs.digital_twin.set_color(panel_right_middle, (255, 255, 255))
        bs.digital_twin.sync()
        time.sleep(10)

    elif bs.bottle_counter() == 1:
        bs.digital_twin.set_all_colors((255, 255, 255))
        bs.digital_twin.set_color(panel_middle_bottom, (255, 0, 0))
        bs.digital_twin.sync()
        time.sleep(10)
    
    elif bs.bottle_counter() == 0: # if all sensors are empty all the panels will turn white
        bs.digital_twin.set_all_colors((255, 255, 255))
        bs.digital_twin.sync()
        time.sleep(10)
