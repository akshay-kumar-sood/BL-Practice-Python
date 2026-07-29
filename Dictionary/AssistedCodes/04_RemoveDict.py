# PROG 3.1: To Remove Data From Dictionary Using del

# Write The Code Here
friends_details={
    'Name':'John',
    'City of Stay':'Mumbai',
    'Pincode':'400088'
}

    # Contact details dictionary
contact_details={
        'Email': 'john.@gmail.com',
        'Phone':'1234567890'
    }

merge_dict=friends_details | contact_details
print("Original Dictionary : ")
print(merge_dict)

if "Pincode" in merge_dict:
  del merge_dict["Pincode"]

print("\nAfter deletion : ")
print(merge_dict)


# 2 ways
# 1. del keyword
# 2. pop keyword