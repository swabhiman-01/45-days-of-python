import time
print(dir(time))
time.sleep(4)
print("done!")
print(time.ctime())
print(time.ctime(23122006))

from datetime import date
print(dir())
today = date.today()
print("Today's date is",today)

print("current month is:",today.month)
print("current year is:",today.year)
print("Today's day is:",today.day)








