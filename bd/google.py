from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
from bd.secrets import parent_folder_id
import json, os

# function to authenticate to Google drive using json credentials
def service_drive(json_file = "bd/service-credentials.json"):
    gauth = GoogleAuth()
    scope = ["https://www.googleapis.com/auth/drive"]
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
    drive = GoogleDrive(gauth)
    return drive

# list all files (excluding folders) in the Google Drive folder
def ListFiles(parent, drive):
    filelist = []

    file_list = drive.ListFile({
        'q': (
            f"'{parent}' in parents and "
            "trashed=false and "
            "mimeType!='application/vnd.google-apps.folder'"
        )
    }).GetList()

    for f in file_list:
        filelist.append({
            "id": f['id'],
            "title": f['title'],
            "title1": f['alternateLink']
        })

    return filelist

def get_photo(name, drive):
    with open('bd/birthdays.json') as d:
        data = json.load(d)

    folder_id = data['birthdays'][f'{name}']['folder_id']
    sub_folder_id = data['birthdays'][f'{name}']['sub_folder_id']
    p_list = ListFiles(folder_id, drive)[0]
    # Saves photo
    photo = drive.CreateFile({'id': p_list['id']})
    photo.GetContentFile(p_list['title'])
    # Moves photo to "Previously Posted" folder
    photo['parents'] = [{"kind": "drive#parentReference", "id": sub_folder_id}]
    photo.Upload()

    return p_list['title']
