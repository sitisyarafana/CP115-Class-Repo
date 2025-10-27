# Takes item name and price from the user
item_name = input("Enter your item_name: ")
price = float(input("Enter price: "))

# Creates variables for quantity (3 items) and tax rate (6%)
quantity = 3
tax_rate = 0.6

# Calculates and displays subtotal, tax amount, and total cost
subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print(f"Item name = {item_name}")
print(f"Item Price = {price}")
print(f"Subtotal = {subtotal}")
print(f"Tax Amount = {tax_amount}")
print(f"Total Cost = {total_cost}")
