from datetime import datetime, timedelta
from pytz import timezone


def write_registration_date(post_date):
    with open('registration_date.txt', 'w') as f:
        f.write(post_date)


def read_registration_date():
    with open('registration_date.txt', 'r') as f:
        return f.read()


def get_datetime(date_string):
    return datetime.strptime(date_string, "%d.%m.%Y %H:%M") + timedelta(minutes=1)


def convert_date(date):
    utc_date = date.replace(tzinfo=timezone('UTC'))
    return utc_date
