import BottleSensors as bs
import NanoleafTestUnit as nl
from threading import Thread
import checkChange as cc
import bottlesSoldTestUnit as bb
import payLeafTestUnit as pl
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

def NanoleafTest() -> None:
    """test function for nanoleaf."""
    print("testing nanoleaf...")
    nl.nanoleaf_indicator()
    time.sleep(1)


testPayLeaf()
testBottlesSold()
NanoleafTest()