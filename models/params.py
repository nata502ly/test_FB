import string
import random

# def random_string(min, maxlen):
#     symbols = string.ascii_lowercase
#     return "Selenium " + "".join([random.choice(symbols) for i in range(random.randrange(min, maxlen))])

def random_birthday(min,max):
    days = range(min, max)
    return random.choice(days)

def random_birthmonth(min,max):
    monthes = range(min, max)
    return random.choice(monthes)

def random_birthyear(min,max):
    years = range(min, max)
    return random.choice(years)

def random_emails(min, max):
    symbols = range(min, max)
    a = random.choice(symbols)
    return "natalia.roshchynatest+" + str(a) + "@gmail.com"

class Data():
    def __init__(self, name = "Monica",
                 surname = "Wayne",
                 email = random_emails(3,100000000000),
                 password = 'qwerty1234567',
                 birthday = random_birthday(1,32),
                 birthmonth = random_birthmonth(1,13),
                 birthyear = random_birthyear(1,114)):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear


