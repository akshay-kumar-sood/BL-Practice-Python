# PROG 4: Dynamic Dictionary Update with User Input for Friend Type Selection

def print_dict(details_dict):
    print(f"Keys: {details_dict.keys()}")
    print(f"Values: {details_dict.values()}")
    print(f"Items: {details_dict.items()}")


def add_default_values():

    friend_details = {
        'Name': 'John Doe',
        'City of Stay': 'Mumbai',
        'Pincode': '400088'
    }

    # Add Country with default value India
    friend_details.setdefault('Country', 'India')

    # Add Friend-Type initially with empty value
    friend_details.setdefault('Friend-Type', '')

    friend_type_options = ["School", "College", "Neighbourhood"]

    # Print dictionary
    print("Dictionary after adding default values:")
    print_dict(friend_details)

    # Ask user to select Friend Type
    print("\nSelect Friend Type:")

    for i, option in enumerate(friend_type_options, start=1):
        print(f"{i}. {option}")

    choice = int(input("Enter the number corresponding to the Friend Type: "))

    # Check choice
    if 1 <= choice <= len(friend_type_options):
        friend_details['Friend-Type'] = friend_type_options[choice - 1]

        print("\nDictionary after setting 'Friend-Type':")
        print_dict(friend_details)
    else:
        print("Invalid choice")


add_default_values()