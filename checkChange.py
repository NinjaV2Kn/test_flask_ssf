import asyncio
import requests
import Nanoleaf as nls

class Bottle:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value != self._amount:
            self._amount = value
            self.on_amount_changed(value)

    def on_amount_changed(self, new_amount):
        print(f"Bottle amount changed to {new_amount}")
        nls.nanoleaf_indicator()

async def bottle_amount_monitor(bottle):
    while True:
        # Simulate some asynchronous operation
        await asyncio.sleep(1)

        # Check if the bottle amount has changed
        new_amount = get_updated_bottle_amount()
        bottle.amount = new_amount

def get_updated_bottle_amount():
    import BottleSensors as bs
    return bs.bottle_counter()

def change_nanoleaf_color():
    pass


# Start the bottle amount monitor automatically when the module is imported
initial_amount = 16
bottle = Bottle(initial_amount)
monitor_task = asyncio.create_task(bottle_amount_monitor(bottle))
