position = input()
overtime_hours = int(input())
is_weekend = input()

# Define base hourly rates
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18
else:
    hourly_rate = 0   # default if invalid position

# Overtime pay (1.5x base hourly rate)
overtime_pay = overtime_hours * (1.5 * hourly_rate)

# Weekend bonus (additional RM5/hour if weekend)
if is_weekend == "Yes":
    overtime_pay += overtime_hours * 5

# Total pay = overtime pay only (since task only asks for overtime calc)
total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)