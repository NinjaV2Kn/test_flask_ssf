import BottleSensors as bs
import asyncio
import Nanoleaf as nls
import checkChange as cc

async def main() -> None:
    """main function."""
    try:
        bs.setup_GPIO()

        print("setup complete")
        print("press CTRL+C to exit")

        bottle_amount_old = 0

        cc.changed()

    except KeyboardInterrupt:
        bs.GPIO.cleanup()

asyncio.run(main())