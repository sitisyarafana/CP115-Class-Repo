# Solution: Skip number 3 with continue
total = 0

for number in range(5):
    print(f'Processing: {number}')

    if number == 3:
        print('Skipping 3!')
        continue  # Skip to next iteration

    total += number  # This line skipped when continue executes
    print(f'Added {number}. Current total: {total}')  # This too

print(f'Final total: {total}')  # Python continues here after each iteration