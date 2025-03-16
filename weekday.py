
from datetime import date, datetime
import calendar

def weekday():
    todays_date = date.today()
    y = todays_date.year
    m = todays_date.month
    d = todays_date.day
    week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    weekday= calendar.weekday(y,m,d)
    print(week_days[weekday])
    hour = int(datetime.now().hour)
    min = int(datetime.now().minute)
    time = int(datetime.now().hour),int(datetime.now().minute)
    print(time)

    
    
    
    

weekday()