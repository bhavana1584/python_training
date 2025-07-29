# Input DOB from the user and output age
import datetime as dt

dob = input("Enter date of birth dd-mm-yyyy: ")
dob_year = dob[-4:]
dob_month = dob[-7:-6]
dob_day = dob[-10:-9]

x = dt.datetime.now()

def calcAge():
    c_year = x.strftime("%Y")
    c_month = x.strftime("%m")
    c_day = x.strftime("%d")
    year = int(c_year)-int(dob_year)-1
    month = int(c_month)-int(dob_month)
    day = int(c_day)-int(dob_day)
    print(f"Age = {year} years, {month} months, {day} days")

calcAge()