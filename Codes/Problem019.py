from time import time
start = time()

def is_leap_year(year):
    #returns number of days of Feb
    if year % 400 == 0:
        return 29
    if year % 4 == 0:
        if year % 100 == 0:
            return 28
        else:
            return 29
    return 28

def day_starting_1_jan_1901():
    #yield days of week
    days_of_week = ['Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Monday']
    while True:
        for day in days_of_week:
            yield day
j = day_starting_1_jan_1901()

first_days = []
for year in range(1901,2001):
    for month in range(1,13):
        if month in [1,3,5,7,8,10,12]:
            for day in range(1,32):
                day_of_week = next(j)
                if day == 1:
                    #appending first day of months
                    first_days.append(day_of_week)
        elif month in [4,6,9,11]:
            for day in range(1,31):
                day_of_week = next(j)
                if day == 1:
                    #appending first day of months
                    first_days.append(day_of_week)
        elif month in [2]:
            for day in range(1,is_leap_year(year)+1):
                day_of_week = next(j)
                if day == 1:
                    #appending first day of months
                    first_days.append(day_of_week)

print("We had",first_days.count('Sunday'),"Sundays in twentieth century")

print("it took {} seconds".format(time() - start))
