# PROG 3: Club Membership Renewal Manager

# Write The Code Here
# PROG 3: Club Membership Renewal Manager

current_input = input(
    "Enter the names of current members (comma-separated): "
)

renewed_input = input(
    "Enter the names of renewed members (comma-separated): "
)

current_members = set()
renewed_members = set()

for name in current_input.split(","):
    current_members.add(name.strip().lower())

for name in renewed_input.split(","):
    renewed_members.add(name.strip().lower())

# Keep members that exist in only one of the two sets
current_members.symmetric_difference_update(renewed_members)

print("\nUpdated club members list:")

for name in current_members:
    print(name.title())