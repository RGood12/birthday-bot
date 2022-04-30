from datetime import datetime
from time import strptime
import json

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))


def keyfunc(date):
    return (date - datetime.today()).days

def nearest_bday(date_schedule, today):
    dates = date_schedule
    search_dates = [date for date in dates if date >= today]
    date = min(search_dates, key=keyfunc)
    return ((date - today).days+1), date.strftime('%Y-%m-%d')


def all_bdays():
    # defines today, and current year
    today = datetime.today()
    currYear = today.year
    
    # reads birthdays.json file 
    f = open('bd/birthdays.json')
    data = json.load(f)

    bday, all_bdays = [], []
    for key, value in data['birthdays'].items():

        age = (currYear - int(key[:4]))
        bday = key[5:].replace('-', '/')
        all_bdays.append(f"{value['buddy']}: {bday} - Turning: {age} in {currYear}")
    
    all_bdays = '\n'.join(all_bdays)
    return all_bdays


def get_nearest_bday():

    # defines today, and current year
    today = datetime.today()
    currYear = today.year

    # reads birthdays.json file 
    f = open('bd/birthdays.json')
    data = json.load(f)

    # creates a list of the birthdays from the .json file
    birthday_list = list(data['birthdays'].keys())
    # converts the birthdays to datetime, then replaces the birth year with the current year for calculation
    birthday_list_current = [datetime.strptime(x,'%Y-%m-%d') for x in birthday_list]
    birthday_list_current = [x.replace(year=currYear) for x in birthday_list_current]

    # combines actual birthdate with birthdate + current year for easy lookup
    res = dict(zip(birthday_list, birthday_list_current))

    # calculates days until the nearest birthday, and the date (in the current year)
    days_until, date = nearest_bday(birthday_list_current, today)

    # looks up the actual birthday from the current year since it's been converted
    actual_bday = list(res.keys())[list(res.values()).index(datetime.strptime(date,'%Y-%m-%d'))]
    buddy = data['birthdays'][actual_bday]['buddy']

    short_date = actual_bday[5:].replace('-', '/')

    return days_until, buddy, short_date


def birthdays_this_month():
    # defines today, and current year
    currMonth = datetime.now().month

    # reads birthdays.json file 
    f = open('bd/birthdays.json')
    data = json.load(f)


    date = []
    buddy = []
    for key, value in data['birthdays'].items():

        month = key[5:]
        month = int(month[:2])

        if month == currMonth:
            date.append(key)
            buddy.append(value)

    total = len(date)
    if total != 0:
        filtered_dict = {key: value for key, value in data['birthdays'].items() if key in date}

        birthdays_this_month = []
        for i in range(0, len(date)):
            birthdays_this_month.append(f"{buddy[i]['buddy']}'s on {date[i][5:].replace('-', '/')}")

        birthdays_this_month = ', '.join(birthdays_this_month)

        return total, birthdays_this_month
    if total == 0:
        return total


def month_conversion(month):
    try:
        month = month[:3]
        month = strptime(month,'%b').tm_mon
    except:
        month = int(month)

    return month


def birthdays_given_month(month):

    currMonth = month_conversion(month)

    # reads birthdays.json file 
    f = open('bd/birthdays.json')
    data = json.load(f)


    date = []
    buddy = []
    for key, value in data['birthdays'].items():

        month = key[5:]
        month = int(month[:2])

        if month == currMonth:
            date.append(key)
            buddy.append(value)

    total = len(date)
    if total != 0:
        filtered_dict = {key: value for key, value in data['birthdays'].items() if key in date}

        birthdays_this_month = []
        for i in range(0, len(date)):
            birthdays_this_month.append(f"{buddy[i]['buddy']}'s on {date[i][5:].replace('-', '/')}")

        birthdays_this_month = '\n'.join(birthdays_this_month)

        return total, birthdays_this_month, currMonth
    if total == 0:
        return total, currMonth

