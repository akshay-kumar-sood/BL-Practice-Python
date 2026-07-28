import datetime

today = datetime.date.today()

start_date = today + datetime.timedelta(days=7 - today.weekday())
completion_date = start_date + datetime.timedelta(weeks=12)

print("Fellowship start date:", start_date)
print("Fellowship completion date:", completion_date)