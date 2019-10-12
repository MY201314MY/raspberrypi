#!/usr/bin/python
from __future__ import print_function

from time import gmtime, strftime, sleep
from bluepy.btle import Scanner, DefaultDelegate, BTLEException
import sys

x = 0
class ScanDelegate(DefaultDelegate):

    def handleDiscovery(self, dev, isNewDev, isNewData):
        global x;
        x+=1
        print("NO.{0} {1}".format(x, dev.addr))
        if dev.addr == "30:ae:a4:12:cb:56":
            print("Master, ESP32's Mongoose Bluetooth found.")
            print("NO.{0} {1}".format(x, dev.addr))
            exit(1)

scanner = Scanner().withDelegate(ScanDelegate())
scanner.scan(10, passive=True)
