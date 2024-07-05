from bd.google import service_drive
from bd.secrets import parent_folder_id, sub_folder_id
import json, os

def upload_file(file_name, buddy_name, msg, submitter_name):
    
    drive = service_drive()

    if msg and submitter_name:
        msg = f"{msg}\n\n-- {submitter_name}"

    if msg and not submitter_name:
        msg = f"{msg}\n\n-- Anonymous ;)"

    with open('birthdays.json') as d:
        data = json.load(d)

    folder_id = data['birthdays'][f'{buddy_name}']['folder_id']
    # Create a file instance and set its metadata
    file = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}], 'mimeType':'image/jpeg'})

    # Set the contents of the file directly
    file.SetContentFile(file_name)

    # Set the description of the file if provided
    if msg:
        file['description'] = msg

    # Upload the file
    file.Upload()

    # Get the file ID
    uploaded_file_id = file['id']

    return uploaded_file_id
