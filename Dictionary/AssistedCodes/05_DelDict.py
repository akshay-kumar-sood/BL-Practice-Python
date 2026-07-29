# PROG 3.2: To Remove Data From Dictionary Using pop

# Write The Code Here
# PROG 3.2: To Remove Data From Dictionary Using pop

# Write The Code Here
# Friend's details dictionary
friend_details = {
    "Name": "Franz Kafka",
    "City of Stay": "Prague",
    "Pincode": "10001"
}

# Additional information dictionary
additional_info = {
    "Email": "franz.kafka@example.com",
    "Phone": "123-456-7890"
}

# Merge dictionaries
merged_dict = {**friend_details, **additional_info}

print(f"Original Dictionary: {merged_dict}\n")

# Remove pincode from the merged dictionary
merged_dict.pop("Pincode")

# Print merged dictionary after removing pincode
print("Merged Dictionary after removing pincode using pop:")
print(merged_dict)
