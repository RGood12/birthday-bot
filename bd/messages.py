from datetime import date
from datetime import datetime
from bd.secrets import *
from bd.groupme import *
from bd.calculations import *


def David_and_Alex():

    age = date_suffix(datetime.today().year - 1996)

    send_message(f"🎂🌟Happy {age} birthday, Alex and David!!🌟🎂\n\nHope you both have a great day! Love you buddies!", bot_id)

def send_bday_message():

    today = datetime.today().strftime("%m-%d")
    date_exceptions = ['08-09']
    
    if today not in date_exceptions:
        try:
            msg, gmID, name, name_len = bday_today()
            pic = f'buddy_pics/{name}/headshot.png'
            pic_url = gm_image_service(pic)
            combined(msg, bot_id, gmID, name_len, pic_url)
        except:
            pass

    elif today == '08-09':
        David_and_Alex()
