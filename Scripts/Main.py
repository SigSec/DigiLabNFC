"""
Project: DigiLab NFC Login - http://www.digilabhub.co.uk/
Developer: Justinas Grigas - https://sigsec.github.io/
Version: 0.0.1 - 21:18 30/04/2018
"""
from sys import exc_info
from time import strftime
import nfc_manager
import drive_manager


def log(msg):
    print(strftime('[%H:%M:%S  %d/%m/%Y] {}'.format(msg)))


def setup_accounts():
    accounts_file = drive_manager.pull_accounts(auth)
    accounts_file = accounts_file.split('\n')
    accounts = []
    for account in accounts_file:
        account = account.strip('\r')
        account = account.split(',')
        accounts.append(account)

    return accounts


if __name__ == '__main__':
    log('App Started.')

    auth = drive_manager.authorise('../Files/credentials.json')
    setup_accounts()
    """
    clf = nfc_manager.init('072f:2200')

    try:
        while True:
            tag = nfc_manager.poll(clf)
            if tag is not None:
                print('Tag')

    except IOError:
        log('NFC sensor is not connected.')
    except KeyboardInterrupt:
        log('Program stopped by Admin.')
    except:
        print(exc_info())

    nfc_manager.stop(clf)
    """
