"""
Project: DigiLab NFC Login - http://www.digilabhub.co.uk/
Developer: Justinas Grigas - https://sigsec.github.io/
Version: 0.0.1 - 21:18 30/04/2018
"""

from nfc import ContactlessFrontend
from nfc.clf import RemoteTarget


def init(device):
    clf = ContactlessFrontend()
    clf.open('usb:%s' % device)
    return clf


def poll(clf):
    tag = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'), iterations=20, interval=0.3)
    return tag


def stop(clf):
    clf.close()

