import BottleSensors as bs
from nanoleafapi import Nanoleaf, NanoleafDigitalTwin
import json

try:
    with open('config.json', 'r') as file:
        config = json.load(file)
        ip = (config['ipCounter'])
except FileNotFoundError:
    print("CONFIG FILE NOT FOUND")

nl = Nanoleaf(ip) # setup nanoleaf
digital_twin = NanoleafDigitalTwin(nl) # setup nanoleaf digital twin(used to control each individuial nanoleaf)

def nanoleaf_indicator() -> None:
    """shows you on the nanoleafes how many bottles are in the fridge(only works with 16 sensors and with only 6 nanoleafes)."""

    # each nanoleaf panel has a diffrent id so you can control each panel individuialy.
    panel_middle_bottom = 55455
    panel_left_bottom = 27581
    panel_right_bottom = 41647
    panel_left_middle = 5517
    panel_right_middle = 1967
    panel_top = 54208

    x = [
        [], # case 0
        [(panel_middle_bottom, (255, 0, 0))], # nanoleaf set 1
        [
            (panel_top, (255, 255, 255)),
            (panel_left_middle, (255, 255, 255)), #case 2
            (panel_right_middle, (255, 255, 255))
        ],
        [(panel_top, (255, 255, 255))], # case 3
        [], # case 4
        [(panel_right_bottom, (255, 100, 0))],# case 5
        [
            (panel_right_bottom, (255, 100, 0)),
            (panel_middle_bottom, (255, 100, 0)) # case 6
        ],
        [
            (panel_right_middle, (255, 0, 0)),
            (panel_left_middle, (255, 0, 0)), # case 7
            (panel_top, (255, 0, 0))
        ],
        [
            (panel_left_middle, (255, 0, 0)), # case 8
            (panel_top, (255, 0, 0))
        ],
        [
            (panel_top, (255, 0, 0)) # case 9
        ],
        [], # case 10
        [(panel_right_bottom, (0, 255, 0))], # case 11
        [
            (panel_right_bottom, (0, 255, 0)), # case 12
            (panel_middle_bottom, (0, 255, 0))
        ],
        [
            (panel_right_middle, (255, 100, 0)),
            (panel_left_middle, (255, 100, 0)), # case 13
            (panel_top, (255, 100, 0))
        ],
        [
            (panel_left_middle, (255, 100, 0)),
            (panel_top, (255, 100, 0)) # case 14
        ],
        [(panel_top, (255, 100, 0))] # case 15
    ]

    try:
        count = bs.bottle_counter() # get the bottle count from the bottle counter function

        match count:
            case 16: # if all sensors are occupied all the panels will turn Green
                digital_twin.set_all_colors((0, 255, 0)) # set all panels to green
            
            case 15: # if 15 sensors are occupied all the panels will turn Green and the top panel will turn orange
                digital_twin.set_all_colors((0, 255, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1]) # set the top panel to orange 

            case 14: # if 14 sensors are occupied all the panels will turn Green and the top panel and the left middle panel will turn orange
                digital_twin.set_all_colors((0, 255, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])
                
            case 13: # if 13 sensors are occupied all the panels will turn Green and the top panel, the left middle panel and the right middle panel will turn orange
                digital_twin.set_all_colors((0, 255, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 12: # 
                digital_twin.set_all_colors((255, 100, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 11:
                digital_twin.set_all_colors((255, 100, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 10: # if 10 sensors are occupied all the panels will turn orange
                digital_twin.set_all_colors((255, 100, 0))

            case 9:
                digital_twin.set_all_colors((255, 100, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])
            
            case 8:
                digital_twin.set_all_colors((255, 100, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 7:
                digital_twin.set_all_colors((255, 100, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 6:
                digital_twin.set_all_colors((255, 0, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 5:
                digital_twin.set_all_colors((255, 0, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 4: # if 4 sensors are occupied all the panels will turn red
                digital_twin.set_all_colors((255, 0, 0))

            case 3:
                digital_twin.set_all_colors((255, 0, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 2:
                digital_twin.set_all_colors((255, 0, 0))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])

            case 1:
                digital_twin.set_all_colors((255, 255, 255))
                for panel in x[count]:
                    digital_twin.set_color(panel[0], panel[1])
            
            case 0: # if all sensors are empty all the panels will turn white
                digital_twin.set_all_colors((255, 255, 255))

        digital_twin.sync()

    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    nanoleaf_indicator() # run the function
