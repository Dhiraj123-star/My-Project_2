from datetime import datetime

year = int(input("Year of birth: "))
month = int(input("Month of birth: "))
date = int(input("Day of birth: "))

now =datetime.now()
current_day= now.day
current_month= now.month
current_year=now.year

month_values= [31,28,31,30,31,30,31,31,30,31,30,31]

if(date>current_day):
    current_month=current_month-1
    current_day=current_day+month_values[month-1]

if (month> current_month):
    current_year=current_year-1
    current_month=current_month+12

cal_day= current_day-date
cal_month= current_month-month
cal_year= current_year-year

print("You are {} years {} months {} days old ".format(cal_year,cal_month,cal_day))