# Dictionary

# used to data mapping
# order 
# no duplicate key
# keys are immutable and case sensitive

# syntax
fruits_dict={
    'Apple':'Red',
    'Banana':'Yellow'
}

print(fruits_dict)

# access keys
print(fruits_dict.keys())

# access values
print(fruits_dict.values())

# access both key and values
print(fruits_dict.items())

# search 
print("Banana" in fruits_dict)


# delete 
# 2 ways 
# 1. del keyword

data = {
    'Name': 'John',
    'City of Stay': 'Mumbai',
    'Pincode': '400088'
}

del data["Name"]

# 2. pop keyword
data.pop("Pincode")

print(data)

# DYnamic dictionary update










# dict.keys()
# dict.values()
# dict.items()
# del 
# pop
# clear
 