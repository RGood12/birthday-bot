from datetime import datetime
from calendar import month_name
from bd.calculations import *
from bd.groupme import *
from bd.secrets import bot_id


def bb1_response():

    buddies = generate_buddies()
    
    nearest = nearest_bday(buddies)
    birthday = datetime.strptime(nearest.birthday, '%Y-%m-%d')

    send_message(f"The next buddy birthday is {nearest.name}\'s, in {nearest.days_until} day(s) on {birthday.strftime('%B')} {date_suffix(birthday.day)}!", bot_id)


def bb2_response():
    
    buddies = generate_buddies()
    total = len(bdays_in_month(buddies, datetime.today().month))
    bdays = '\n∙ '.join(bdays_in_month(buddies, datetime.today().month))
    
    if total > 1:
        send_message(f"There are {total} birthdays this month:\n\n∙ {bdays}", bot_id)
    if total == 1:
        send_message(f"Well, look who's special! There's only {total} birthday this month:\n\n∙ {bdays}", bot_id)
    if total == 0:
            send_message(f"There are no birthdays this month!", bot_id)


def bb3_response(text):

    months = {m.lower() for m in month_name[1:]}
    request_month = next((word for word in text.split() if word.lower() in months), None)
    month_num = datetime.strptime(request_month, "%B").month
    
    buddies = generate_buddies()
    bdays = bdays_in_month(buddies, month_num)
    
    total = len(bdays)
    bdays = '\n∙ '.join(bdays)

    if total > 1:
        send_message(f"There are {total} birthdays in {request_month}:\n\n∙ {bdays}", bot_id)
    if total == 1:
        send_message(f"Well, look who's special! There's only {total} birthday in {request_month}:\n\n∙ {bdays}", bot_id)
    if total == 0:
        send_message(f"There are no birthdays in {request_month}!", bot_id)
