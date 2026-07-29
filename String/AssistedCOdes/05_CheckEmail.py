import re
email=input("ENter your email id : ")

pattern=r"^[\w]+(@gmail\.com|@yahoo.in)$"

if len(re.findall(pattern,email))!=0:
  print(f"{email} is an Valid email address")
else:
  print(f"{email} is not valid")