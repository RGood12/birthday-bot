from datetime import datetime
from bd.google import *
from bd.calculations import *
from bd.email_alerts import *

def photo_checker():

    buddies = generate_buddies()
    nearest = nearest_bday(buddies)

    if nearest.days_until > 0 and nearest.days_until < 8:
        with open('bd/birthdays.json') as d:
            data = json.load(d)

        folder_id = data['birthdays'][nearest.name]['folder_id']

        drive = service_drive(json_file = "bd/service-credentials.json")
        try:
            p_list = ListFiles(folder_id, drive)[0]
        except:
            send_alert(f"⚠️Buddy Missing Photo⚠️: {nearest.name}",
            f"{nearest.name} has an upcoming birthday in {nearest.days_until} days, but is missing a photo in Google Drive.")

photo_checker()
