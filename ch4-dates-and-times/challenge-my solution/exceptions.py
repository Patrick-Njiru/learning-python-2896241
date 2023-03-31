class Error(Exception):
    """ Base class for other exceptions"""
    pass
class DayRangeError(Error):
    """ This exception will be raised when the value for the day is not between 0 and 6 """
    pass
class MonthRangeError(Error):
    """ This exception will be raised when the value for the month is not between 1 and 12 """
    pass
class YearError(Error):
    """ This exception will be raised when the value for the year is a negative number """
    pass