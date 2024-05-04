import datetime
import pandas as pd #псевдоним

#from datetime import datetime

d_one = datetime.datetime.utcnow()

print(d_one)

d_two = datetime.datetime.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(d_two.strftime("%d/%m/%y %I:%M"))

three_hours = datetime.timedelta(hours=3)
two_days = datetime.timedelta(2)

print(three_hours,two_days, three_hours + two_days, datetime.datetime.now() - datetime.timedelta(hours=3))