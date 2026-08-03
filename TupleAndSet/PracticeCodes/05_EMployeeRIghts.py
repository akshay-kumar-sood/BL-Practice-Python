# PROG 5: Employee Access Rights Update Based on Current Staff

# Write The Code Here

# PROG 5: Employee Access Rights Update

access_input = input(
    "Enter the employees with access rights (comma-separated): "
)

current_input = input(
    "Enter the current employees (comma-separated): "
)

access_rights = set()
current_employees = set()

# Make names case-insensitive
for name in access_input.split(","):
    access_rights.add(name.strip().lower())

for name in current_input.split(","):
    current_employees.add(name.strip().lower())

# Keep only employees present in both sets
access_rights.intersection_update(current_employees)

print("\nUpdated Access Rights List:")

for employee in access_rights:
    print(employee.title())