"""
Project: DigiLab NFC Login - http://www.digilabhub.co.uk/
Developer: Justinas Grigas - https://sigsec.github.io/
Version: 0.0.1 - 21:18 30/04/2018
"""

from nfc import ContactlessFrontend
from nfc.clf import RemoteTarget
from Main import log


def init(device):
    log('Initialising the NFC.')
    clf = ContactlessFrontend()
    try:
        clf.open('usb:%s' % device)
    except IOError:
        log('NFC sensor must be replugged.')
        exit()
    return clf


def poll(clf):
    log('Polling for an NFC tag.')
    try:
        tag = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'), iterations=5, interval=0.3)
    except:
        clf.close()
    return tag


def stop(clf):
    log('Stopping the NFC.')
    clf.close()

