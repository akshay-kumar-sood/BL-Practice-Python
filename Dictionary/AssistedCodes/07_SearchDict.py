# PROG 5: To Search The Data In Dictionary

# Dictionary containing details of 5 friends
friends = {
    "Friend1": [
        {"City": "New York", "Pincode": "10001"},
        {"Email": "friend1@example.com", "PhoneNumber": "1234567890"}
    ],

    "Friend2": [
        {"City": "Los Angeles", "Pincode": "90001"},
        {"Email": "friend2@example.com", "PhoneNumber": "2345678901"}
    ],

    "Friend3": [
        {"City": "Chicago", "Pincode": "60601"},
        {"Email": "friend3@example.com", "PhoneNumber": "3456789012"}
    ],

    "Friend4": [
        {"City": "Houston", "Pincode": "77001"},
        {"Email": "friend4@example.com", "PhoneNumber": "4567890123"}
    ],

    "Friend5": [
        {"City": "Miami", "Pincode": "33101"},
        {"Email": "friend5@example.com", "PhoneNumber": "5678901234"}
    ]
}


# Take friend's name from user
name = input(
    "Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): "
)

# Ask which detail the user wants
detail = input(
    "Enter detail type (City/Pincode/Email/PhoneNumber): "
)


# Check if friend exists in the dictionary
if name not in friends:
    print("Friend not found!")


# City and Pincode are stored in the first dictionary (index 0)
elif detail == "City" or detail == "Pincode":
    print(f"{name}'s {detail}: {friends[name][0][detail]}")


# Email and PhoneNumber are stored in the second dictionary (index 1)
elif detail == "Email" or detail == "PhoneNumber":
    print(f"{name}'s {detail}: {friends[name][1][detail]}")


# If user enters something other than the available details
else:
    print("Invalid detail type!")