import json
from bd.messages import date_suffix, David_and_Alex, send_bday_message

if __name__ == "__main__":

    f = open('bd/birthdays.json')
    data = json.load(f)

    send_bday_message(data)


