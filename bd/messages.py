from datetime import date
from discord import Webhook, RequestsWebhookAdapter
from datetime import datetime
from bd.secrets import bot_id, port, discord_webhook
from bd.groupme import *


def date_suffix(day):
    if 3 < day < 21 or 23 < day < 31:
        return f'{day}th'
    else:
        return {1: f'{day}st', 2: f'{day}nd', 3: f'{day}rd'}[day % 10]


def David_and_Alex():

    age = date_suffix(currYear - 1996)

    send_message(f"🎂🌟Happy {age} birthday, Alex and David!!🌟🎂\n\nHope you both have a great day! Love you buddies!", bot_id)

def Brock():
    age = date_suffix(currYear - 1995)

    webhook = Webhook.from_url(discord_webhook, adapter=RequestsWebhookAdapter())
    webhook.send(f"🎂🌟Happy {age} birthday, Brock (Funnier Alex)!🌟🎂\n\nHope you have a great day!!")

def send_bday_message(data):

    today = date.today()
    currYear = today.year
    today = str(today)[5:]

    date_exceptions = ['05-17', '08-09']

    #Loop along dictionary keys
    for key, value in data['birthdays'].items():

        birthday = key[5:]
        age = date_suffix(currYear - int(key[:4]))
        name_len = (len(value['buddy'])+1)
        buddy = value['buddy']
        gmID = value['gmID']

        if birthday == today and today not in date_exceptions:
            send_message_mention(f"@{buddy} 🎂🌟Happy {age} birthday, {value['buddy']}!!🌟🎂\n\nHope you have a great day! Love you buddy!", bot_id, gmID, name_len)
        elif today == '08-09':
            David_and_Alex()
            break
        elif today == '05-17':
            Brock()
            break
