import calendar
from datetime import date
user_input = raw_input()
tokens = user_input.split(" ")
month = int(tokens[0])
week = int(tokens[1])

week_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
date = week_names[date(2009, week, month).weekday()] 
print(date)
