# Import entire modules
import math

# Getting user input (always returns a string)
radius = float(input("Enter your radius: "))

# Using imported modules
circle_area = math.pi * (radius ** 2)
circumference_area = 2 * math.pi * radius

# Formatted output using string concatenation
print()
print("Area of circle: ", + circle_area)
print("Circumference of circle: ", + circumference_area)