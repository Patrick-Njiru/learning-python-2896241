#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the calendar module
import calendar

# TODO: create a plain text calendar
""" calendar.SUNDAY inidicates the week starts on Sunday """
c = calendar.TextCalendar(calendar.SUNDAY)
'''  
c.formatyear(year, w = horizontal space between days, l = vertical space bewteen days,c = horizontal space between months, m = number of months per row) 
c.formatmonth(year, month, horizontal space between days, vertical space between days) 
'''
print(c.formatyear(0, 5, 3, 15, 4))
# print(c.formatmonth(2023, 3, 5, 3))


# TODO: create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
""" 
c.formatmonth(year, month, horizontal spacing, vertical spacing) 
"""
# print(hc.formatmonth(2023, 3))

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2022, 4):
#     print(i)
  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#     print(name)

# for day in calendar.day_name:
#     print(day)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

# print("Team metings will be on")
# for m in range(1,13):
#     cal = calendar.monthcalendar(2023, m)
#     week_one = cal[0]
#     week_two = cal[1]
#     if week_one[calendar.FRIDAY] != 0: 
#         meeting_day = week_one[calendar.FRIDAY]
#     else: 
#         meeting_day = week_two[calendar.FRIDAY]
#     print(calendar.month_name[m], meeting_day)