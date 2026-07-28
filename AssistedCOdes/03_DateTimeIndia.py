import datetime
import pytz

india_timezone = pytz.timezone("Asia/Kolkata")

current_datetime = datetime.datetime.now(india_timezone)

print("Current Date and Time (IST):", current_datetime)

print("Formatted Date and Time (IST):")
print("Month (as full name):", current_datetime.strftime("%B"))
print("Weekday (as full name):", current_datetime.strftime("%A"))
print("Year (as four digits):", current_datetime.strftime("%Y"))

print("Month (as abbreviated name):", current_datetime.strftime("%b"))
print("Weekday (as abbreviated name):", current_datetime.strftime("%a"))
print("Year (as two digits):", current_datetime.strftime("%y"))

print("Day of the month (01-31):", current_datetime.strftime("%d"))
print("Hour (24-hour clock):", current_datetime.strftime("%H"))
print("Hour (12-hour clock):", current_datetime.strftime("%I"))
print("Minute (00-59):", current_datetime.strftime("%M"))
print("Second (00-59):", current_datetime.strftime("%S"))
print("AM/PM indicator:", current_datetime.strftime("%p"))