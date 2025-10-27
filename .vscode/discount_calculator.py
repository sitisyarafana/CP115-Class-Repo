# NAME : SITI SYARAFANA BINTI SABDIN
# MATRIC NO : MC2515113654

Age = int(input("Enter your age:"))
Ticket_Price = float(input("Enter the price of the movie ticket:"))

# Check input whether invalid or not
if Age < 0:
    print("Invalid Input")
elif Ticket_Price < 0:
    print("Invalid Input")
else:    #determine category and discount based on age
    if Age <= 12:
        Category = "Children"
        Discount = 0.5
    elif Age >= 13 and Age <= 17:
        Category = "Teenager"
        Discount = 0.25
    else:
        Category = "Adult"
        Discount = 0.0
    
    # Calculate discounted price
    Discounted_Price = Ticket_Price - (Ticket_Price * Discount)

    # Display output
    print(f"You are eligible for the {Category} discount ({Discount * 100:.0f}% off)")
    print(f"Discounted ticket price: ${Discounted_Price:.2f}")