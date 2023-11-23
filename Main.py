import BottleSensors as bs
import asyncio
import checkChange as cc

cc = cc.changes()
def main() -> None:
    """main function."""
    try:
        bs.setup_GPIO()

        print("setup complete")
        print("press CTRL+C to exit")

        cc.run()

    except KeyboardInterrupt:
        bs.GPIO.cleanup()

main()