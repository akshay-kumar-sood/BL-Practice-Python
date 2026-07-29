# PROG 2: Swap Case

# Write The Code Here

def transform(str):
  res=""
  for i in range(0,len(str)):
    if str[i].islower():
      res=res+str[i].upper()
    elif str[i].isupper():
      res=res+str[i].lower()
    else:
      res=res+str[i]
  return res


str=input("Input String : ")
res=transform(str)
print(f"Output String : {res}")      


# way 2 :

def shortcut(str):
  return str.swapcase()

result=shortcut(str)
print(f"Output String using shorthand way : {result}")