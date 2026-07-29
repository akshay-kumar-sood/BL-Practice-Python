# PROG 4: To Use Regex To Search Digits

# Write The Code Here
import re

str="fA7c33de85"
testcase2="Engineer"

digit=re.findall(r"\d",str)
print(f"Digit found in the string are : {digit}")

no_digit=re.findall(r"\d",testcase2)
if len(no_digit)==0:
  print("No digit found in the string")