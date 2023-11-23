import BottleSensors as bs
import Nanoleaf as nls
import time

def main():
    """main function."""
    try:
        bs.setup_GPIO()

        print("setup complete")
        print("press CTRL+C to exit")

        while True:
            bs.bottle_counter()

            time.sleep(0.1)

            nls.nanoleaf_indicator()

    except KeyboardInterrupt:
        bs.GPIO.cleanup()

main()
