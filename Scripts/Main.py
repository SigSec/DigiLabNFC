"""
Project: DigiLab NFC Login - http://www.digilabhub.co.uk/
Developer: Justinas Grigas - https://sigsec.github.io/
Version: 0.0.1 - 21:18 30/04/2018
"""
from time import strftime, sleep
import traceback
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


def check_nfc(accounts, nfc_tag):
    for account in accounts:
        for nfc_code in account[7:]:
            if nfc_code.upper() == nfc_tag:
                return 1
    return 0


if __name__ == '__main__':
    log('App Started.')

    auth = drive_manager.authorise('../Files/credentials.json')
    accounts = setup_accounts()

    clf = nfc_manager.init('072f:2200')

    try:
        while True:
            tag = nfc_manager.poll(clf)
            if tag is not None:
                # Account has already been created.
                if check_nfc(accounts, tag) == 1:
                    print('old')
                # Account is new.
                else:
                    print('new')
                sleep(1)

    except IOError:
        log('NFC sensor is not connected.')
    except KeyboardInterrupt:
        log('Program stopped by Admin.')
    except:
        traceback.print_exc()

    nfc_manager.stop(clf)
