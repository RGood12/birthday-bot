from datetime import date
from datetime import datetime
from bd.secrets import *
from bd.groupme import *
from bd.google import *
from bd.calculations import *
from bd.email_alerts import *
import os
import logging

def setup_logger():
    logging.basicConfig(filename='bot.log', level=logging.ERROR,
                        format="%(asctime)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

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
            send_nophoto_alert(nearest.name, nearest.days_until)

def send_bday_message():

    today = datetime.today().strftime("%m-%d")
    # gets message and buddy info if bday is today
    blist = bday_today()
    
    if blist is None:
        photo_checker()
        quit()

    try:
        for index, buddy in enumerate(blist):
            msg, gmID, name, name_len = blist[index]
            drive = service_drive()

            # gets a photo of buddy from google respective buddy drive folder
            pic = get_photo(name, drive)
            pic_stats = os.stat(pic)
            logging.error(f"INFO: Successfully grabbed picture for {name}: {round(pic_stats.st_size / (1024 * 1024), 2)} MB")
            # uploads that photo to GroupMe's image service
            pic_url = gm_image_service(pic)
            logging.error(f"INFO: GM Image Service URL: {pic_url}")

            # sends message to GroupMe
            combined(msg, bot_id, gmID, name_len, pic_url)

            # deletes photo previously downloaded
            os.remove(pic)
            logging.error(f"INFO: Picture for {name} successfully removed")
    except IndexError:
        send_error_alert(name, "No photo available in Google Drive")
        logging.error(f"ERROR: No photo available in Google Drive")
        logging.error(f"Data: {gmID}, {name}, {name_len}")
        logging.error("-------------------------------")
        quit()
    except Exception as e:
        send_error_alert(name, e)
        logging.error(f"ERROR: {e}")
        logging.error(f"Data: {gmID}, {name}, {name_len}")
        logging.error("-------------------------------")
        quit()

setup_logger()
