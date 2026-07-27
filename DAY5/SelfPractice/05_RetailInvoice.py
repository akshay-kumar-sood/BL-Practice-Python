# PROG 5:  Retail Invoicing App

# Write The Code Here
import random

HOUSEHOLD_GST = 0.05
PROCESSED_FOOD_GST = 0.12

items = [
    "Banana", "Tomato", "Soap", "Rice", "Masala",
    "Biscuits", "Milk", "Bread", "Oil", "Shampoo",
    "Sugar", "Tea", "Juice", "Detergent", "Chips"
]

prices = [
    15, 10, 40, 60, 200,
    30, 50, 35, 150, 120,
    45, 100, 80, 90, 20
]

gst = [
    0.05, 0.05, 0.05, 0.05, 0.12,
    0.12, 0.05, 0.05, 0.05, 0.05,
    0.05, 0.12, 0.12, 0.05, 0.12
]

buyer = input("Enter the buyer name: ")

# Select 3 different items
selected_items = random.sample(range(15), 3)

total = 0
total_gst = 0

print("\nRetail Invoicing App")
print("----------------------------------------")
print("Buyer Name:", buyer)
print("----------------------------------------")
print("Item\t\tQty\tPrice")
print("----------------------------------------")

for index in selected_items:

    quantity = random.randint(1, 5)

    amount = prices[index] * quantity
    gst_amount = amount * gst[index]

    total += amount
    total_gst += gst_amount

    print(items[index], "\t\t", quantity, "\t", prices[index])

final_bill = total + total_gst

print("----------------------------------------")
print("Total\t\t\tRs", round(total, 2))
print("GST\t\t\tRs", round(total_gst, 2))
print("----------------------------------------")
print("Total Billing\t\tRs", round(final_bill, 2))
print("----------------------------------------")