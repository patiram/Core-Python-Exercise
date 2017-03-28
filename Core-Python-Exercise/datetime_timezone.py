import datetime

d = datetime.date(2016, 7, 24)
#datetime.date(2016, 07, 24) wrong
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)

#Monday 0 Sunday 6
#ISO Monday 1 Sunday 7
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)

print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = datel + date2
# how old I am
bday = datetime.date(1990, 5, 8)

till_day = tday - bday

print(till_day.days)

print(till_day.total_seconds())


t = datetime.time(9, 30, 45, 100000) #hour min second microsec

print(t.hour)


t = datetime.datetime(2016, 7, 26, 9, 30, 45, 100000) #year month days hour min second microsec

print(t)
print(t.date())
print(t.year)
print(t.month)
print(t.day)


tdelta = datetime.timedelta(days=7) # hours

print(t + tdelta)




dt_today = datetime.datetime.today()

dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

#pytz is recommended by python.org to work with time zone manipulation

import pytz

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)



dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
print(dt_utcnow)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Central Standard Time'))

# import time
# from datetime import datetime

# import pytz # $ pip install pytz
# from tzlocal import get_localzone # $ pip install tzlocal

# # get local timezone    
# local_tz = get_localzone() 
# print(local_tz)

# # test it
# # utc_now, now = datetime.utcnow(), datetime.now()
# ts = time.time()
# utc_now, now = datetime.utcfromtimestamp(ts), datetime.fromtimestamp(ts)

# local_now = utc_now.replace(tzinfo=pytz.utc).astimezone(local_tz) # utc -> local
# assert local_now.replace(tzinfo=None) == now

# To get local time zone using module import dateutil.tz and datetime
import dateutil.tz
localtz = dateutil.tz.tzlocal()
print(localtz.tzname(datetime.datetime.now()))

# To get local time zone using import pytz and datetime modules
from pytz import reference
localtime = reference.LocalTimezone()
print(localtime)
today = datetime.datetime.now()
print(today)
print(localtime.tzname(today))



# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Central'))

# All pytz time zone

from pytz import all_timezones

print (len(all_timezones))
for zone in all_timezones:
	if 'US' in zone:
		print(zone)
		print (dt_utcnow.astimezone(pytz.timezone(zone)))
		# if 'US/Cen'in zone:
		# 	print (dt_utcnow.astimezone(pytz.timezone(zone)))


# dt_ktm = dt_utcnow.astimezone(pytz.timezone('Asia/Kathmandu'))
# print(dt_ktm)
# dt_katm = dt_utcnow.astimezone(pytz.timezone('Asia/Katmandu'))
# print(dt_katm)

#time zone convert
dt_central = datetime.datetime.now()
central_tz = pytz.timezone('US/Central')
dt_central = central_tz.localize(dt_central)
print(dt_central)
dt_east = dt_central.astimezone(pytz.timezone('US/Eastern'))

print(dt_east)
print(dt_central.isoformat())
print(dt_central.strftime('%B %d, %Y'))

#String to datetime format to standard format

dt_string = 'September 03, 2016'
dt = datetime.datetime.strptime(dt_string, '%B %d, %Y')
print(dt)
print(dt.strftime('%B %d, %Y'))