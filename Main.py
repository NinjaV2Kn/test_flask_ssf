import BottleSensors as bs
import asyncio
import checkChange as cc

cc = cc.changes()
async def main() -> None:
    """main function."""
    try:
        bs.setup_GPIO()

        print("setup complete")
        print("press CTRL+C to exit")

        cc.changed()

    except KeyboardInterrupt:
        bs.GPIO.cleanup()

asyncio.run(main())