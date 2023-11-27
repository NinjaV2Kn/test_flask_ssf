import Nanoleaf as nls
import BottleSensors as bs
from time import sleep

def check():
    bottle_amount_old = 0

    while True:
        bottle_amount = bs.check_bottles()
        if bottle_amount != bottle_amount_old:
            bottle_amount_old = bottle_amount
            nls.nanoleaf_indicator()
            sleep(0.5)
        bs.bottle_counter()