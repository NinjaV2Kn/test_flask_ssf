import asyncio
import BottleSensors as bs
import Nanoleaf as nls

class changes:
    """keeps track of the bottle amount and checks if it has changed."""
    
    def __init__(self) -> None:
        self.bottle_amount_old = 0
        self.bottle_amount = bs.bottle_counter()

    async def amount(self) -> None:
        """keeps track of the bottle amount."""
        try:
            while True:
                self.bottle_amount = bs.bottle_counter()
                await asyncio.sleep(0.1)
        
        except Exception as e:
            print(e)

    async def changed(self) -> None:
        """Checks if the bottle amount has changed."""
        try:
            while True:  # Added loop here
                if self.bottle_amount != self.bottle_amount_old:
                    nls.nanoleaf_indicator()
                    await asyncio.sleep(2)
                    self.bottle_amount_old = self.bottle_amount
                await asyncio.sleep(0.1)  # Added sleep here to prevent busy-waiting

        except Exception as e:
            print(e)

    def run(self):
        loop = asyncio.get_event_loop() # Set event loop
        loop.run_until_complete(asyncio.wait([self.changed(), self.amount()]))
        loop.close() # if both loops are completed the program closes