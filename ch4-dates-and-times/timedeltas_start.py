#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# TODO: construct a basic timedelta and print it
# print(timedelta(days=365, hours = 5, minutes = 1))

# TODO: print today's date
# now = datetime.now()
# print('today is', now)

# TODO: print today's date one year from now
# print("1 year from now it will be", str(now + timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
# print("In two weeks and three days it will be", str(now + timedelta(weeks=2, days=3)))

# TODO: calculate the date 1 week ago, formatted as a string
# a_week_ago = now - timedelta(weeks=1)
# print(a_week_ago.strftime("1 week ago, it was %A %B, %Y"))
### How many days until April Fools' Day?


# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
today = date.today()
afd = date(today.year, 4, 1)

if today > afd:
    print(f"This year's April Fools already passed by {(today-afd).days}")
    afd = afd.replace( year = today.year + 1)
    # print(f"The next one is due in {(afd-today).days} days")
print("April Fools day is due in", str((afd-today).days), "days")

# TODO: Now calculate the amount of time until April Fool's Day  

