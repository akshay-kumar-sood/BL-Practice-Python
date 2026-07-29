# PROG 2: Update The Dictionary

# Write The Code Here
def merge_dict():
  friends_details={
        'Name': input("ENter you name : "),
        'city' : input("Enter your city : "),
        'pincode':input("ENter your pincode")
    }

    # Contact details dictionary
  contact_details={
        'Email': 'john.@gmail.com',
        'Phone':'1234567890'
    }

  # Method 1: using update() method
  merge_dict=friends_details.copy()
  merge_dict.update(contact_details)
  #print(merge_dict)

  #Method 2: using unpacking() **
  merge_dict_unpacking={**friends_details,**contact_details}
  #print(merge_dict_unpacking)


  # Method 3: Using | operator
  merge_dict_union= friends_details | contact_details
  #print(merge_dict_union)

   # Method 3: Using | operator union
  merge_dict_union= friends_details | contact_details
  #print(merge_dict_union)

  # method 4 : using \= operator
  merged_dict_ior=friends_details.copy()
  merged_dict_ior |=contact_details
  #print(merged_dict_ior)

  print("\nMerged DIctionary using update()")
  print_dict(merge_dict)

  print("\nMerged DIctionary using unpacking(**)")
  print_dict(merge_dict_unpacking)

  print("\nMerged DIctionary using | operator")
  print_dict(merge_dict_union)

  print("\nMerged DIctionary using |= operator ")
  print_dict(merged_dict_ior)


def print_dict(details_dict):
  print(f"\nUsing Keys methods : {details_dict.keys()}")
  print(f"Using  values methods : {details_dict.values()}")
  print(f"Using items methods : {details_dict.items()}")


merge_dict()


# various ways
# 1. copy update
# 2. or operator |
# 3. **
# 4. |= 