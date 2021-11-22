from datetime import date
from datetime import time
from datetime import datetime

#today = date.today()
#print("Today's date is ", today)
#print("Date Components : ", today.day, today.month, today.year)
#print("Today's weekday ", today.weekday())


today = datetime.now()

#print("Today's date and time : ", today)
#t = datetime.time(datetime.now())
#print("Current time is ", t)


#wd=date.weekday(today)
##Days start at 0 for monday
#days= ["Monday", "Tuesday", "Wednesday",
#       "Thursday", "Friday",
#       "Saturday", "Sunday"]
#print("Today is day number %d" % wd)
#print("which is a " + days[wd])

'''
now = datetime.now()
print(now.strftime("%Y"))
print(now.strftime("%y"))

print(now.strftime("%A %d %B %y"))

print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))

print(now.strftime("%I:%M:%S %p"))
print(now.strftime("%H:%M"))

'''
from datetime import timedelta

print(timedelta(days=365, hours=8, minutes=15))

print("One year from now it will be : ", str(datetime.now() + timedelta(365)))
print("In one week and four days it will be : ",
      str(datetime.now() + timedelta(weeks=1, days=4)))

today = date.today()
nyd = date(today.year, 1, 1)
if nyd < today:
    print("New Year day was %d days ago." % ((today - nyd).days))


