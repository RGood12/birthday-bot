from datetime import date
from datetime import datetime
from bd.secrets import *
from bd.groupme import *
from bd.google import *
from bd.calculations import *
import os
import logging

def setup_logger():
    logging.basicConfig(filename='bot.log', level=logging.ERROR,
                        format="%(asctime)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

def send_bday_message():

    today = datetime.today().strftime("%m-%d")

    # gets message and buddy info if bday is today
    blist = bday_today()

    if blist is None:
        quit()

    try:
        for index, buddy in enumerate(blist):
            msg, gmID, name, name_len = blist[index]
            drive = service_drive()

            # gets a photo of buddy from google respective buddy drive folder
            pic = get_photo(name, drive)
            logging.error(f"INFO: Successfully grabbed picture for {name}: {pic}")

            # uploads that photo to GroupMe's image service
            pic_url = gm_image_service(pic)
            logging.error(f"INFO: GM Image Service URL: {pic_url}")

            # sends message to GroupMe
            combined(msg, bot_id, gmID, name_len, pic_url)

            # deletes photo previously downloaded
            os.remove(pic)
            logging.error(f"INFO: Picture for {name} successfully removed")
    except Exception as e:
        logging.error(f"ERROR: {e}")
        logging.error(f"Data: {gmID}, {name}, {name_len}")
        logging.error("-------------------------------")
        quit()

setup_logger()
