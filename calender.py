import calendar
m,d,y = input().split()
print(calendar.day_name[calendar.weekday(int(y), int(m), int(d))].upper())

#Given timestamps, print the absolute difference (in seconds) between them.

import email.utils
import time
import datetime

for i in range(int(input())):
    print(int(round(float(email.utils.mktime_tz(email.utils.parsedate_tz(input()))) - float(
        email.utils.mktime_tz(email.utils.parsedate_tz(input()))))))
