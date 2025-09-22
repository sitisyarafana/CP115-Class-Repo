current_reading = int(input())
previous_reading = int(input())

# TODO: Your code here

cubic_meter = int(input("Enter cubic meter"))

# rate structure
if cubic_meter <= 20:
    consumption = cubic_meter * 0.57
elif cubic_meter <= 35:
    consumption = cubic_meter * 1.03
else :
    consumption = cubic_meter * 1.40

# calculate water cost
water_cost = consumption * (current_reading + previous_reading)

# calculate total bill
total_bill = water_cost + 8.00 + 2.00

print(consumption)
print(water_cost)
print(total_bill)