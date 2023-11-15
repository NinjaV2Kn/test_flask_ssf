from nanoleafapi import Nanoleaf, NanoleafDigitalTwin
from time import sleep

nl = Nanoleaf("192.168.30.132")
digital_twin = NanoleafDigitalTwin(nl)

panel_middle_bottom = 55455
panel_left_bottom = 27581
panel_right_bottom = 41647
panel_left_middle = 5517
panel_right_middle = 1967
panel_top = 54208


effect_full = {
        "command": "add",
        "animType": "static",
        "animData": "6 54208 1 255 100 0 0 20 5517 1 255 100 0 0 20 1967 1 255 100 0 0 20 27581 1 255 100 0 0 20 55455 1 255 100 0 0 20 41647 1 255 100 0 0 20",
        "loop": False,
        "palette": [{
            "hue": 0,
            "saturation": 100,
            "brightness": 0
        }, {
            "hue": 30,
            "saturation": 100,
            "brightness": 10
        }],
        "colorType": "HSB"
        }

nl.write_effect(effect_full)
