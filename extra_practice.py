""" 1
my_file = open("newfile.txt", "r")

list_contents = my_file.read()
print("read:", list_contents)

array_contents = my_file.readlines()
print ("readlines: ", array_contents)
"""

""" 2 predicts tommorow
from datetime import date
today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday()+1)%7])

"""

""" 3
from datetime import date
today = date.today()
# Option A: correct
tomorrow = today+timedelta(days=1)
# Option B: wrong because if tommorow is in the next month the variable tommorow will still inidicate this month
tomorrow = date(today.year,today.month,today.day+1)
"""

""" 4 
from datetime import datetime, date
print(datetime.date(datetime.now()) == date.today())
"""


'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'
