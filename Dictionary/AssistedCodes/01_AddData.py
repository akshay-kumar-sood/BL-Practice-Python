# PROG 1.1: Add Data In Dictionary With Hard-Coded Values

# Write The Code Here

def print_dict(friends_details):
  print(f"TYpe of friends_details : {type(friends_details)}")
  # print each detail one by one using keys
  print("\nPrinting details using keys : ")
  for key in friends_details:
    print(f"{key} : {friends_details[key]}")


friends_details={
    'Name':'John',
    'City of Stay':'Mumbai',
    'Pincode':'400088'
}

print_dict(friends_details)

print("\nPrinting using items : ")

for key,value in friends_details.items():
  print(f"{key} : {value}")
