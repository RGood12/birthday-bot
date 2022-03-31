from datetime import datetime
from calendar import month_name
from bd.calculations import nearest, keyfunc, nearest_bday, all_bdays, get_nearest_bday, birthdays_this_month, month_conversion, birthdays_given_month
from bd.groupme import send_message
from bd.secrets import bot_id


def bb1_response():

    days_until, buddy, short_date = get_nearest_bday()
    send_message(f"The next buddy birthday is {buddy}\'s, in {days_until} day(s) on {short_date}!", bot_id)


def bb2_response():
    try:
        totals, bdays = birthdays_this_month()
        if totals > 1:
            send_message(f"There are {totals} birthdays this month: {bdays}", bot_id)
        if totals == 1:
            send_message(f"Well, look who's special! There's only {totals} birthday this month: {bdays}", bot_id)
    except:
        totals = birthdays_this_month()
        if totals == 0:
            send_message(f"There are no birthdays this month!", bot_id)


def bb3_response(text):

    months = {m.lower() for m in month_name[1:]}
    request_month = next((word for word in text.split() if word.lower() in months), None)

    try:
        totals, bdays, month = birthdays_given_month(request_month)
        month = datetime(1, month, 8).strftime("%B")
        if totals == 1:
            send_message(f"Well, look who's special! There's only {totals} birthday in {month}: {bdays}", bot_id)
        if totals > 1:
            send_message(f"There are {totals} birthdays in {month}:\n\n{bdays}", bot_id)
    except:
        totals, month = birthdays_given_month(request_month)
        month = datetime(1, month, 8).strftime("%B")
        if totals == 0:
            send_message(f"There are no buddy birthdays in {month}!", bot_id)
