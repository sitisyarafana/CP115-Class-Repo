age = int(input())
accident_count = int(input())

# Define base premium
if age <= 25:
    base_premium = 2400
elif 25 <= age <= 50:
    base_premium = 1800
else:
    base_premium = 2000

#define penalty
if accident_count == 0:
    penalty = 0
    discount = 0.1
elif 1 <= accident_count <= 2:
    penalty = 300
else:
    penalty = 600






    
print(base_premium)
print(final_premium)
print(discount_amount)