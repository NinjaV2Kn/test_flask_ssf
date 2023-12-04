import Nanoleaf as nls
import BottleSensors as bs
from time import sleep

def check() -> None:
    bottle_amount_old = 0
    try:
        while True:
            bottle_amount = bs.bottle_counter()
            if bottle_amount != bottle_amount_old:
                bottle_amount_old = bottle_amount
                nls.nanoleaf_indicator()
                sleep(0.5)
            bs.bottle_counter()
    except Exception as e:
        print(e)