# script that pulls the current page of artists

import requests
from datetime import date, datetime, timedelta

def get_date(startdate, weekday):
    """
    @startdate: given date, in format '2013-05-25'
    @weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
    """
    d = datetime.strptime(startdate, '%Y-%m-%d')
    t = timedelta((7 + weekday - d.weekday()) % 7)

    return (d + t).strftime('%Y-%m-%d')

today = date.today()
d = today.strftime("%Y-%m-%d")
print("Today's date:", d)

# get dates of the weekend days and add them to list
wdates = []

wdates.append(get_date(d, 4)) # 4 = Friday
wdates.append(get_date(d, 5)) # 5 = Saturday
wdates.append(get_date(d, 6)) # 6 = Sunday

print(wdates)

# pull html code for weekend days
for date in wdates:
    r = requests.get(f"https://www.wwoz.org/calendar/livewire-music?date={date}")

    filename = f"./calendar_data/index-{date}.html"
    
    with open(filename, 'w') as fd: 
        fd.write(r.text)