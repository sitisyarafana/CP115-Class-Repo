monthly_usage = input()
bill = input()

# Define discount based on monthly_usage
if monthly_usage < 50:
    discount = 0
elif 50 <= monthly_usage <= 100:
    discount = 0.05
else:
    discount = 0.20

# calculate amount of the bill
total_bill = bill - (bill * discount)

# display amount of the bill
print(total_bill)