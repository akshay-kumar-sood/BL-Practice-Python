# PROG 1.2: Add Data In Dictionary With User Input

# Write The Code Here
# PROG 1.1: Add Data In Dictionary With Hardter-Coded Values

# Write The Code Here

def print_dict():
  friends_details={
      'Name': input("ENter you name : "),
      'city' : input("Enter your city : "),
      'pincode':input("ENter your pincode")
  }

  print(f"TYpe of friends_details : {type(friends_details)}")
  # print each detail one by one using keys
  print("\nPrinting details using keys : ")
  for key in friends_details:
    print(f"{key} : {friends_details[key]}")


friends_details={
      'Name': input("ENter you name : "),
      'city' : input("Enter your city : "),
      'pincode':input("ENter your pincode")
  }

print_dict()

print("\nPrinting using items : ")

for key,value in friends_details.items():
  print(f"{key} : {value}")
