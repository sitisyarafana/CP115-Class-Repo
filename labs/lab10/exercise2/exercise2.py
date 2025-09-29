age = int(input())
accident_count = int(input())

# Your code here
# Determine the base premium
if age < 25:
    base_premium = 2400
elif 25 <= age <= 50:
    base_premium = 1800
else:
    base_premium = 2000

# Calculate the accident penalty
if accident_count == 0:
    accident_penalty = 0
elif 1 <= accident_count <= 2:
    accident_penalty = 300
else:
    accident_penalty = 600

# Calculate the good driver discount using integer arithmetic
discount_amount = 0
if accident_count == 0:
    # Multiply by 10 and then integer-divide by 100
    discount_amount = ((base_premium + accident_penalty) * 10) // 100

# Calculate the final premium
final_premium = (base_premium + accident_penalty) - discount_amount

print(base_premium)
print(final_premium)
print(discount_amount)