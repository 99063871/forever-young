import datetime
now = datetime.datetime.now()

nowHour = int(now.hour)
nowHourTxt = str(now.hour)
if nowHour < 12:
    print(nowHourTxt + "AM")

elif nowHour >= 12:
    print(nowHourTxt + "PM")