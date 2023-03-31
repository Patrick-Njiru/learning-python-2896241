# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar
from exceptions import DayRangeError, MonthRangeError, YearError

rerun = True
while rerun:
    print("\nWhich day of the week do you want to count? \n")

    for i in range(0,7):  print(f"{i}: {calendar.day_name[i]} \n")

    print("or 'exit' to quit")
    day = input("? ")

    if day.lower() == "exit":
        rerun = False
        break
    else:
        try:
            day, month, year = int(day), int(input("Enter month: ")), int(input("Enter year: "))

            if day not in range(0, 7): raise DayRangeError
            elif month not in range(1,13): raise MonthRangeError
            elif year < 0: raise YearError
            else:
                cal = calendar.monthcalendar(year, month)
                no_of_days = 0
                for week in cal:
                    if week[day] != 0: no_of_days += 1
                print(
                    f"\n{calendar.TextCalendar(calendar.SUNDAY).formatmonth(year, month, 5, 2)} \nThere are {no_of_days} {calendar.day_name[day].upper()}s in {calendar.month_name[month].upper()}, {year} \n"
                    )
                
        except ValueError as e: print(f"\n{e}. \nAdd a number. \n-------------- \n")
        except DayRangeError: print("\nThe day's value should be between 0 and 6. \n")
        except MonthRangeError: print("\nThe month's value should be between 0 and 12. \n")
        except YearError: print("\nInvalid year. Minimum accepted value is 0 \n")