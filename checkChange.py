import asyncio
import BottleSensors as bs
import Nanoleaf as nls

bottle_amount_old = 0
bottle_amount = bs.bottle_counter()

async def change() -> None:
    """keeps track of the bottle amount."""
    try:
        bottle_amount_old = 0
        while True:
            bottle_amount = bs.bottle_counter()
    
    finally:
        pass

async def changed() -> None:
    """Checks if the bottle amount has changed."""
    bottle_amount_old = 0
    try:
        if bottle_amount != bottle_amount_old:
            nls.nanoleaf_indicator()
            await asyncio.sleep(2)
            bottle_amount_old = bottle_amount
            
    finally:
        pass