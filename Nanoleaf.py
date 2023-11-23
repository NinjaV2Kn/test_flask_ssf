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
        digital_twin.set_all_colors((0, 255, 0)) # set all panels to green
        digital_twin.sync() # sync the nanoleafes to set the colors

    elif bs.bottle_counter() == 15: # if 15 sensors are occupied all the panels will turn Green and the top panel will turn orange
        digital_twin.set_all_colors((0, 255, 0))
        digital_twin.set_color(panel_top, (255, 100, 0)) # set the top panel to orange
        digital_twin.sync()

    elif bs.bottle_counter() == 14: # if 14 sensors are occupied all the panels will turn Green and the top panel and the left middle panel will turn orange
        digital_twin.set_all_colors((0, 255, 0))
        digital_twin.set_color(panel_top, (255, 100, 0))
        digital_twin.set_color(panel_left_middle, (255, 100, 0))
        digital_twin.sync()
        
    elif bs.bottle_counter() == 13: # if 13 sensors are occupied all the panels will turn Green and the top panel, the left middle panel and the right middle panel will turn orange
        digital_twin.set_all_colors((0, 255, 0))
        digital_twin.set_color(panel_top, (255, 100, 0))
        digital_twin.set_color(panel_left_middle, (255, 100, 0))
        digital_twin.set_color(panel_right_middle, (255, 100, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 12: # 
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_middle_bottom, (0, 255, 0))
        digital_twin.set_color(panel_right_bottom, (0, 255, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 11:
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_right_bottom, (0, 255, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 10: # if 10 sensors are occupied all the panels will turn orange
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 9:
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_top, (255, 0, 0))
        digital_twin.sync()
    
    elif bs.bottle_counter() == 8:
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_top, (255, 0, 0))
        digital_twin.set_color(panel_left_middle, (255, 0, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 7:
        digital_twin.set_all_colors((255, 100, 0))
        digital_twin.set_color(panel_top, (255, 0, 0))
        digital_twin.set_color(panel_left_middle, (255, 0, 0))
        digital_twin.set_color(panel_right_middle, (255, 0, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 6:
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.set_color(panel_middle_bottom, (255, 100, 0))
        digital_twin.set_color(panel_right_bottom, (255, 100, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 5:
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.set_color(panel_right_bottom, (255, 100, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 4: # if 4 sensors are occupied all the panels will turn red
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.sync()

    elif bs.bottle_counter() == 3:
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.set_color(panel_top, (255, 255, 255))
        digital_twin.sync()

    elif bs.bottle_counter() == 2:
        digital_twin.set_all_colors((255, 0, 0))
        digital_twin.set_color(panel_top, (255, 255, 255))
        digital_twin.set_color(panel_left_middle, (255, 255, 255))
        digital_twin.set_color(panel_right_middle, (255, 255, 255))
        digital_twin.sync()

    elif bs.bottle_counter() == 1:
        digital_twin.set_all_colors((255, 255, 255))
        digital_twin.set_color(panel_middle_bottom, (255, 0, 0))
        digital_twin.sync()
    
    elif bs.bottle_counter() == 0: # if all sensors are empty all the panels will turn white
        digital_twin.set_all_colors((255, 255, 255))
        digital_twin.sync()