from nanoleafapi import Nanoleaf, NanoleafDigitalTwin
import time
import json

try:
    with open('config.json', 'r') as file:
        config = json.load(file)
        ip = (config['ipPayLeaf'])
except FileNotFoundError:
    print("CONFIG FILE NOT FOUND")

nlp = Nanoleaf(ip)
nlp_twin = NanoleafDigitalTwin(nlp)

def payLeaf() -> None:
    """Lets the nanoleafes blink"""
    pause = 1/5
    current_effect = nlp.get_current_effect()
    for _ in range(3):
        nlp_twin.set_all_colors((255, 100, 0))
        nlp_twin.sync()
        time.sleep(pause)
        nlp_twin.set_all_colors((0, 0, 0))
        nlp_twin.sync()
        time.sleep(pause)    
    nlp.set_effect(current_effect)


def payLeaf2():
    pause = 1/3
    current_effect = nlp.get_current_effect()
    nlp.set_color((217, 142, 27))
    for _ in range(2):
        nlp.set_brightness(60)
        time.sleep(pause)
        nlp.set_brightness(20)
        time.sleep(pause)
    nlp.set_effect(current_effect)
    nlp.set_brightness(50)

if __name__ == "__main__":
    payLeaf2()