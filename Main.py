import BottleSensors as bs
import asyncio
import checkChange as cc


def main() -> None:
    """main function."""
    try:
        bs.setup_GPIO()

        print("setup complete")
        print("press CTRL+C to exit")
        while True:
            cc.check()        
        
    except KeyboardInterrupt:
        bs.GPIO.cleanup()

main()