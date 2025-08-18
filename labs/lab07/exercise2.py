# Convert these to f-strings
product_name = "Laptop"
price = 1299.99
quantity = 2
total = price * quantity

# Old way (convert these to f-strings)
print("Product: " + product_name)
print("Price: $" + str(price))
print("Quantity: " + str(quantity))
print("Total: $" + str(total))

print(f"Product: {product_name}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${total}")