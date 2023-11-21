from datetime import date, datetime
from operator import attrgetter
import json, os, random


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

def gen_message(name, age):
    
    messages = [f"@{name} Happy {age} Birthday, bucket head!! 🎉🍰\n\nTo celebrate, here's a favorite picture of you that always brings a smile to my face.",
    f"@{name} To the biggest goofball I know, Happy {age} Birthday!! 🎂🎁\n\nHere's a favorite picture of you, capturing your infectious spirit.",
    f"@{name} Another year older, ya nut! Happy {age} Birthday!! 🥳🎈\n\nAnd here's a cherished image of you to remind us of the good times we've had.",
    f"@{name} Happy {age} Birthday, bud-ee!! 🎈🎉\n\nAs a special gift, here's a favorite picture of you to mark this special day.",
    f"@{name} Wishing you a day filled with sweetness and joy, goofball!! 🎁🍰 Happy {age} Birthday!\n\nHere's a special picture of you to celebrate.",
    f"@{name} Happy {age} Birthday, you nut!! 🥳🎂\n\nMay your day be as extraordinary as you are. Here's a cherished image to remind you of all the fun times.",
    f"@{name} Another year, another reason to celebrate you, bucket head!! 🎈🎁\n\nHave an amazing {age} birthday and enjoy this special picture of you.",
    f"@{name} To my favorite goofball, Happy {age} Birthday!! 🍰🎉\n\nKeep spreading smiles and laughter. Here's a cherished image of you to remember the good times.",
    f"@{name} Happy {age} Birthday, ya nut!! 🎂🎈\n\nYour uniqueness adds so much flavor to our lives. Enjoy your special day and this special picture.",
    f"@{name} Wishing a fantastic {age} birthday to my dear bud-ee!! 🥳🎁\n\nMay your day be filled with joy and unforgettable moments. Here's a favorite picture to mark this special occasion."]
    
    return random.choice(messages)

def bday_today():
    
    buddies = generate_buddies()
   
    buddies_bday_today = [obj for obj in buddies if obj.days_until == 0]
    if buddies_bday_today:
        blist = []
        for buddy in buddies_bday_today:
            name, age = buddy.name, date_suffix(buddy.age)
            message = gen_message(name, age)
            gm_id = buddy.gm_id
            name_len = len(buddy.name)+1
            blist.append((message, gm_id, name, name_len))
        return blist
    else:
        return None
        
