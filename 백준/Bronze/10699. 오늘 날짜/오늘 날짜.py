import datetime

# hint : 9 시간 차이
today_utc = datetime.datetime.utcnow()
seoul_offset = datetime.timedelta(hours=9)
seoul_today = today_utc + seoul_offset
print(seoul_today.strftime('%Y-%m-%d'))