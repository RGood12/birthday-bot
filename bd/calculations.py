from datetime import date, datetime
from operator import attrgetter
import json


def date_suffix(day):
    if 3 < day < 21 or 23 < day < 31:
        return f'{day}th'
    else:
        return {1: f'{day}st', 2: f'{day}nd', 3: f'{day}rd'}[day % 10]


def init_data():
    # reads birthdays.json file 
    with open('bd/birthdays.json') as d:
        data = json.load(d)
    return data


def age_calc(data, birthday):
    
    today = date.today()
    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


def days_until(birthday):
    
    today = datetime.today()
    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    birthday = birthday.replace(year=today.year)
    
    diff = birthday - today
    return (diff.days+1)


class Buddy():
    
    def __init__(self, name, birthday, age, days_until, gm_id):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.days_until = days_until
        self.gm_id = gm_id
    
    def __repr__(self):
        return '{' + self.name + ', ' + self.birthday + ', ' + str(self.age) + ', ' + str(self.days_until) + ', ' + str(self.gm_id) + '}'


def generate_buddies():
    data = init_data()
    buddies = []
    for i in range(0, len(data['birthdays'])):
        buddies.append(Buddy(list(data['birthdays'])[i], 
                 list(data['birthdays'].values())[i]['birthday'], 
                 age_calc(data, list(data['birthdays'].values())[i]['birthday']), 
                 days_until(list(data['birthdays'].values())[i]['birthday']),
                 list(data['birthdays'].values())[i]['gmID']))
    return buddies


def nearest_bday(buddies):
    
    buddies.sort(key=lambda x: (x.days_until<0, x.days_until))
    return buddies[0]


def bdays_in_month(buddies, month):
    
    birthdays_this_month = []
    
    for i in range(0, len(buddies)):
        
        birthday = datetime.strptime(buddies[i].birthday, '%Y-%m-%d')
        
        if birthday.month == datetime.today().month:
            if birthday.month == month and birthday.day >= datetime.today().day:
                birthdays_this_month.append(f"{buddies[i].name}'s on {birthday.strftime('%B')} {date_suffix(birthday.day)}, turning {buddies[i].age+1}")
            elif birthday.month == month and birthday.day < datetime.today().day:
                birthdays_this_month.append(f"{buddies[i].name}'s on {birthday.strftime('%B')} {date_suffix(birthday.day)}, turned {buddies[i].age}")
            elif birthday.month == month and birthday.day == datetime.today().day:
                birthdays_this_month.append(f"{buddies[i].name}'s on {birthday.strftime('%B')} {date_suffix(birthday.day)}, turning {buddies[i].age+1}")
        
        else:
            if birthday.month == month and birthday.month >= datetime.today().month:
                birthdays_this_month.append(f"{buddies[i].name}'s on {birthday.strftime('%B')} {date_suffix(birthday.day)} - turning {buddies[i].age+1} this year")
            elif birthday.month == month and birthday.month < datetime.today().month:
                birthdays_this_month.append(f"{buddies[i].name}'s on {birthday.strftime('%B')} {date_suffix(birthday.day)} - turned {buddies[i].age} this year")
            elif birthday.month == month and birthday.month == datetime.today().month:
                birthdays_this_month.append(f"{buddies[i].name}'s on {birthday.strftime('%B')} {date_suffix(birthday.day)} - turning {buddies[i].age+1}")
    return birthdays_this_month


def all_bdays():
    
    buddies = generate_buddies()
    buddies.sort(key=attrgetter('name'))

    all_bdays = []
    
    for i in range(0, len(buddies)):
        birthday = datetime.strptime(buddies[i].birthday, '%Y-%m-%d')
        birthday = f"{birthday.strftime('%B')} {date_suffix(birthday.day)}, {birthday.year}"

        all_bdays.append(f"• {buddies[i].name}: {birthday}")

    all_bdays = "\n".join(all_bdays)
    return all_bdays


def bday_today():
    
    buddies = generate_buddies()
    
    for i in range(0, len(buddies)):
        if buddies[i].days_until == 0:
            message = f"@{buddies[i].name} 🎂🌟Happy {date_suffix(buddies[i].age)} birthday, {buddies[i].name}!!🌟🎂\n\nHope you have a great day! Love you buddy!"
            gm_id = buddies[i].gm_id
            name_len = len(buddies[i].name)+1
            return message, gm_id, name_len
