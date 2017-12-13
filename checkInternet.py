#!/usr/bin/python

import os
import urllib2


# Set Variables Here
wifiAdaptor = "wlan0"
ssidName = "MyWiFiSSID"

# Don't modify anything below here
def checkWiFiUp():
    for timeout in [1,5,10,15]:
        try:
            response = urllib2.urlopen('http://google.com',timeout=timeout)
            return True
        except urllib2.URLError as err:
            pass
        return False


if __name__ == "__main__":
    internetOnline = checkWiFiUp()
    if internetOnline == True:
        exit
    elif internetOnline == False:
        os.system('ifconfig {} down'.format(wifiAdaptor))
        os.system('ifconfig {} up'.format(wifiAdaptor))
        os.system('iwconfig {} essid {}'.format(wifiAdaptor, ssidName))
        os.system('dhclient -v {}'.format(wifiAdaptor))
