import BottleSensors as bs
import asyncio
import Nanoleaf as nls

async def main() -> None:
    """main function."""
    try:
        bs.setup_GPIO()

        print("setup complete")
        print("press CTRL+C to exit")

        bottle_amount_old = 0

        while True:
            bottle_amount = bs.bottle_counter()
            if bottle_amount != bottle_amount_old: #check if the bottle amount has changed
                bs.bottle_counter()
                nls.nanoleaf_indicator()

                bottle_amount_old = bottle_amount
                await asyncio.sleep(2) #wait 2 seconds to not overload the nanoleafes

    except KeyboardInterrupt:
        bs.GPIO.cleanup()

main()