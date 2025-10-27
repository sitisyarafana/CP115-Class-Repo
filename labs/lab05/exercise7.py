import math

# Takes one number from the user
Number = int(input("Enter one number: "))

# Calculates and displays: square root, square (power of 2), cube (power of 3), and sine value
# Square root
square_root = math.sqrt(Number)
print(f"Square root: {square_root}")

# Square (power of 2)
square_value = Number ** 2
print(f"Square: {square_value}")

# Cube (power of 3)
cube_value = Number ** 3
print(f"Cube: {cube_value}")

# Sine value (in radians)
sine_value = math.sin(Number)
print(f"Sine value: {sine_value}")