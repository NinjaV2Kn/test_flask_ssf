import asyncio

class Bottle:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, value):
        if value != self._amount:
            self._amount = value
            self.on_amount_changed(value)

    def on_amount_changed(self, new_amount):
        import Nanoleaf as nls
        print(f"Bottle amount changed to {new_amount}")
        nls.nanoleaf_indicator()



async def bottle_amount_monitor(bottle):
    while True:
        # Simulate some asynchronous operation
        await asyncio.sleep(1)

        # Check if the bottle amount has changed
        # In a real-world scenario, you might have some external input or event triggering this check
        new_amount = get_updated_bottle_amount()
        bottle.amount = new_amount


def get_updated_bottle_amount():
    # Simulate getting an updated bottle amount from some external source
    import BottleSensors as bs
    return bs.bottle_counter()


async def main():
    initial_amount = 0
    bottle = Bottle(initial_amount)

    # Start the bottle amount monitor
    monitor_task = asyncio.create_task(bottle_amount_monitor(bottle))

    try:
        # Your main application logic can go here
        # For now, we'll just let the monitor run for a while
        await asyncio.sleep(10)
    finally:
        # Cancel the monitor task when done
        monitor_task.cancel()
        try:
            await monitor_task
        except asyncio.CancelledError:
            pass


if __name__ == "__main__":
    asyncio.run(main())
