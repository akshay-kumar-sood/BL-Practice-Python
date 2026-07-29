# PROG 1: Full Name With Right Case Structure

def transform(first_name, middle_name, last_name):
    full_name = " ".join(filter(None, [first_name, middle_name, last_name]))
    return full_name.title()


first_name=input("ENter first name: ")
middle_name=input("Enter middle name :")
last_name=input("Enter last name : ")

res=transform(first_name,middle_name,last_name)
print(f"Formatted full name is : {res}")

# filter is used to remove empty dtring from the list
# title  is used to make first letter of string uppercase
