total_cost = 0.0
item_count = 0

price = float(input())

# TODO: Your code here

while price >= 0: # condition
    total_cost += price
    item_count += 1
    price = float(input()) # update

print(item_count)
print(f"{total_cost:.2f}")
