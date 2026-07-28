# PROG 6: Calendar Module

# Write The Code Here
import calendar

def print_calendar(month, year):

    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")

    weeks = calendar.monthcalendar(year, month)

    for week in weeks:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            else:
                print(f"{day:2}", end=" ")

        print()


month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year (Ex. 2024): "))

print_calendar(month, year)


# {day:2} means give 2 width for example 2 turn to space 2
# 10 remain 10 as it have 2 space