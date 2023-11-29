import BottleSensors as bs
import Nanoleaf as nl
from threading import Thread
import checkChange as cc
import bottlesSold as bb
import payLeaf as pl
import time

def testPayLeaf() -> None:
    """test function for payLeaf."""
    print("testing payLeaf...")
    pl.payLeaf2()
    time.sleep(1)

def testBottlesSold() -> None:
    """test function for bottlesSold."""
    print("testing bottlesSold...")
    bb.main()
    time.sleep(1)

if __name__ == "__main__":
    testPayLeaf()