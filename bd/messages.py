from datetime import date
from discord import Webhook, RequestsWebhookAdapter
from datetime import datetime
from bd.secrets import *
from bd.groupme import *
from bd.calculations import *


def David_and_Alex():

    age = date_suffix(datetime.today().year - 1996)

    send_message(f"🎂🌟Happy {age} birthday, Alex and David!!🌟🎂\n\nHope you both have a great day! Love you buddies!", bot_id)

def Brock():
    age = date_suffix(datetime.today().year - 1995)

    webhook = Webhook.from_url(discord_webhook, adapter=RequestsWebhookAdapter())
    webhook.send(f"<@{brock_id}> 🎂🌟Happy {age} birthday, Brock (Funnier Alex)!🌟🎂\n\nHope you have a great day!!")

def send_bday_message():

    today = datetime.today().strftime("%m-%d")
    date_exceptions = ['05-17', '08-09']
    
    if today not in date_exceptions:
        try:
            message, gm_id, name_len = bday_today()
            send_message_mention(message, bot_id, gm_id, name_len)
        except:
            pass

    elif today == '08-09':
        David_and_Alex()
    elif today == '05-17':
        Brock()
