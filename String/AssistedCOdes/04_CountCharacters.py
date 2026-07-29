# List comprehension 
# shortcut way

str="assnsh$#5ans@#4"

letter=sum(1 for char in str if char.isalpha())
digit=sum(1 for char in str if char.isdigit())
special=len(str)-(letter+digit)


print(f" Letter in string are : {letter}")
print(f"Digit  in string are : {digit}")
print(f"Special character in string are : {special}")


# python generator 
# expression for item in collection
# x*x for x in list

