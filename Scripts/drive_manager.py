"""
Project: DigiLab NFC Login - http://www.digilabhub.co.uk/
Developer: Justinas Grigas - https://sigsec.github.io/
Version: 0.0.1 - 21:18 30/04/2018
"""

from pydrive.auth import GoogleAuth


def authorise(credentials_file):
    google_auth = GoogleAuth()
    try:
        google_auth.LoadCredentialsFile(credentials_file)
    except IOError:
        print('No Credentials file found.')
    # Check credentials
