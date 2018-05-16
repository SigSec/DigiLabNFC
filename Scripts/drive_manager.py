"""
Project: DigiLab NFC Login - http://www.digilabhub.co.uk/
Developer: Justinas Grigas - https://sigsec.github.io/
Version: 0.0.1 - 21:18 30/04/2018
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import Main


def authorise(credentials_file):
    Main.log('Authorising PyDrive Google Authentication.')
    google_auth = GoogleAuth()
    google_auth.LoadCredentialsFile(credentials_file)
    # Check credentials
    if google_auth.credentials is None:
        # Authenticate credentials if they do not exist.
        google_auth.LocalWebserverAuth()
    elif google_auth.access_token_expired:
        # Refresh credentials if they have expired.
        google_auth.Refresh()
    else:
        # Authorise the credentials otherwise.
        google_auth.Authorize()

    google_auth.SaveCredentialsFile(credentials_file)
    return google_auth


def push_accounts(auth, accounts):
    Main.log('Pushing the current Accounts file to Drive.')
    drive = GoogleDrive(auth)

    # Search for the DigiLab Folder.
    folder_id = None
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for g_file in file_list:
        if g_file['title'] == 'DigiLabNFC' and g_file['mimeType'] == 'application/vnd.google-apps.folder':
            folder_id = g_file['id']
            break

    # Create a folder if it doesn't already exist.
    if folder_id is None:
        Main.log('Creating a new DigilabNFC folder')
        global folder_id
        folder_metadata = {'title': 'DigiLabNFC', 'mimeType': 'application/vnd.google-apps.folder'}
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        folder_id = folder['id']

    # Check if an Account file already exists.
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % (folder_id)}).GetList()
    for g_file in file_list:
        if g_file['title'] == 'Accounts.csv':
            Main.log('Deleting old Accounts.csv file')
            accounts_file = drive.CreateFile({'id': g_file['id']})
            accounts_file.Delete()
            break

    # Upload the Account file
    Main.log('Uploading new Accounts.csv file')
    accounts_file = drive.CreateFile({'title': 'Accounts.csv', 'parents': [{'kind': 'drive#fileLink', 'id': folder_id}]})
    accounts_file.SetContentFile(accounts)
    accounts_file.Upload()


def pull_accounts(auth):
    Main.log('Pulling accounts from web.')
    drive = GoogleDrive(auth)

    # Search for the DigiLab Folder.
    folder_id = None
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for g_file in file_list:
        if g_file['title'] == 'DigiLabNFC' and g_file['mimeType'] == 'application/vnd.google-apps.folder':
            folder_id = g_file['id']
            break

    # Check if an Account file already exists.
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % (folder_id)}).GetList()
    for g_file in file_list:
        if g_file['title'] == 'Accounts.csv' and g_file['mimeType'] == 'text/csv':
            accounts_file = drive.CreateFile({'id': g_file['id'], 'mimeType': g_file['mimeType']})
            return accounts_file.GetContentString()
