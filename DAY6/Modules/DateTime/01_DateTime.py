# Exploring Date time module

# import first
from datetime import datetime,date,time,timedelta

# third party have to create virtual enviroment
# import pytz


# now  we can acces only year month day from it
print(datetime.now())

# today date
print(date.today())

# curr time
print(time(10,30,40))

# deltatime --> add time 
curr_date=date.today()

# now add a week
future=curr_date + timedelta(days=7)

print(f"curr date is : {curr_date} and future is : {future}")


# strftime --> very important --> beautify the output

now=datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%A %d %B %Y"))


# to chnage time zone
# indian time zone

#ist = pytz.timezone("Asia/Kolkata")

#curr_date = datetime.now(ist)
#print(curr_date)

# important method are
# 1. datetime.now()
# 2. strftime()



