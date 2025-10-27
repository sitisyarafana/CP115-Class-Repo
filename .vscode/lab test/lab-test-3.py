# NAME : SITI SYARAFANA BINTI SABDIN
# R
monthly_usage = float(input("Enter monthly usage in RM :"))

discount = 0
total_bill = 0

# Define discount based on monthly_usage
if monthly_usage < 50:
    discount = 0.0
elif monthly_usage <= 100:
    discount = 0.05
else:
    discount = 0.20

# calculate amount of the bill
total_bill = monthly_usage - (monthly_usage * discount)

# display amount of the bill
print(f"Your total bill is:RM {total_bill:.2f}")