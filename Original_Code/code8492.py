from datetime import *

def is_leap(year):
    ""year -> 1 if leap year, else 0.""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
MAX_MONTH = 12
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

year, month, day = [int(i) for i in input().split()]

if is_leap(year):
    days_in_month[2] = 29
    
add_day = int(input())
x, y, z = date(year, month, day), timedelta(day), timedelta(add_day)
y += z

while y.days > days_in_month[month]:
    y -= timedelta(days_in_month[month])
    month += 1
    if month > MAX_MONTH:
        month -= MAX_MONTH
        year += 1
    if is_leap(year):
        days_in_month[2] = 29
    else:
        days_in_month[2] = 28
        
else:
    x = '{} {} {}'.format(year, month, y.days)
print(x) 