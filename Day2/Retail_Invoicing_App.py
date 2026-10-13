
import random

# GST rates
HOUSEHOLD_GST = 0.05
PROCESSED_FOOD_GST = 0.12

# List of 15 items
items = [
    "Banana", "Masala", "Tomato", "Rice", "Soap",
    "Shampoo", "Milk", "Bread", "Biscuits", "Sugar",
    "Oil", "Detergent", "Tea", "Toothpaste", "Cheese"
]

# Corresponding prices
prices = [
    15, 200, 10, 60, 40,
    120, 30, 35, 25, 45,
    150, 90, 80, 55, 100
]

# Corresponding GST categories
gst_categories = [
    "PROCESSED_FOOD", "PROCESSED_FOOD", "PROCESSED_FOOD",
    "PROCESSED_FOOD", "HOUSEHOLD", "HOUSEHOLD",
    "PROCESSED_FOOD", "PROCESSED_FOOD", "PROCESSED_FOOD",
    "PROCESSED_FOOD", "PROCESSED_FOOD", "HOUSEHOLD",
    "PROCESSED_FOOD", "HOUSEHOLD", "PROCESSED_FOOD"
]

# Ask buyer's name
buyer = input("Enter the buyer name: ")

# Randomly select 3 different item indexes
selected = random.sample(range(len(items)), 3)

subtotal = 0
total_gst = 0

print("\nRetail Invoicing App")
print("-" * 40)
print(f"Buyer Name: {buyer}")
print("-" * 40)

print(f"| {'Item':<15} | {'Qty':^5} | {'Price':>8} |")
print("-" * 40)

# Generate bill
for index in selected:
    item = items[index]
    price = prices[index]
    category = gst_categories[index]
    quantity = random.randint(1, 5)

    amount = price * quantity
    subtotal += amount

    if category == "HOUSEHOLD":
        gst_rate = HOUSEHOLD_GST
    else:
        gst_rate = PROCESSED_FOOD_GST

    gst_amount = amount * gst_rate
    total_gst += gst_amount

    print(f"| {item:<15} | {quantity:^5} | {price:>8} |")

print("-" * 40)
print(f"{'Total':<25} Rs {subtotal:.2f}")
print(f"{'GST':<25} Rs {total_gst:.2f}")
print("-" * 40)
print(f"{'Total Billing':<25} Rs {subtotal + total_gst:.2f}")
print("-" * 40)
