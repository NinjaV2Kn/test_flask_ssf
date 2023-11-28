import BottleSensors as bs
import checkChange as cc
import bottlesSold as bb


def main() -> None:
    """main function."""
    try:
        bs.setup_GPIO()

        print("setup complete")
        print("press CTRL+C to exit")
        while True:
            cc.check()        
            bb.main()
    except KeyboardInterrupt:
        bs.GPIO.cleanup()

main()