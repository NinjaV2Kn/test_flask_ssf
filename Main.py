import BottleSensors as bs
from threading import Thread
import checkChange as cc
import bottlesSold as bb
import test_flask.Sensor_test as st


def main() -> None:
    """main function."""
    try:
        bs.setup_GPIO()
        print("Sensor setup complete")

        print("press CTRL+C to exit")
        bb.soldPrint()
        t1 = Thread(target=cc.check)
        t2 = Thread(target=bb.main)
        t1.start()
        t2.start()

        print("starting Webserver...")
        st.startFlask()
        print("startup complete")
        
    except KeyboardInterrupt:
        bs.GPIO.cleanup()

main()