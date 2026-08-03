# PROG 4: Club Membership Renewal Manager

# Write The Code Here
# PROG 4: Email Marketing Duplicate Checker

current_input = input(
    "Enter the current subscribers' emails (comma-separated): "
)

new_input = input(
    "Enter the new sign-ups' emails (comma-separated): "
)

current_subscribers = set()
new_signups = set()

for email in current_input.split(","):
    current_subscribers.add(email.strip().lower())

for email in new_input.split(","):
    new_signups.add(email.strip().lower())


if current_subscribers.isdisjoint(new_signups):
    print("There are no common email addresses between current subscribers and new sign-ups.")

else:
    common_emails = current_subscribers.intersection(new_signups)

    print("The following email addresses are present in both lists:")

    for email in common_emails:
        print(email)