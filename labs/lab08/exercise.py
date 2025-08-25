# Test assignment operators
score = 100
print(f"Starting score: {score}")

score += 10     # Add 10
print(f"After += 10: {score}")

score -= 5      # Subtract 5
print(f"After -= 5: {score}")

score *= 2      # Multiply by 2
print(f"After *= 2: {score}")

score //= 3     # Floor division by 3
print(f"After //= 3: {score}")

score %= 15     # Modulus by 15
print(f"After %= 15: {score}")

score **= 2     # Square it
print(f"After **= 2: {score}")
# Sequential execution example
print("Step 1: Starting program")
x = 10
print(f"Step 2: x is now {x}")
x = x * 2
print(f"Step 3: x is now {x}")
y = x + 5
print(f"Step 4: y is now {y}")
result = x + y
print(f"Step 5: Final result is {result}")
# Order matters in sequential programming
name = "Ali"
age = 20
student_id = "2024001"

# Build information step by step
full_info = f"Name: {name}"
full_info = full_info + f", Age: {age}"
full_info = full_info + f", ID: {student_id}"

print(full_info)
# This code proves sequential execution
print("Line 1: This will run")
print("Line 2: This will also run") 
x = 10
print(f"Line 3: x = {x}")
y = x * 2
print(f"Line 4: y = {y}")
print("Line 5: All good so far")

# This line has an intentional error
# print(unknown_variable)  # This will cause an error