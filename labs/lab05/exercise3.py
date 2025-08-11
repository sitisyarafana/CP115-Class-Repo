# Import random modules
import random

# Takes the student's class name from the user
class_name = input("Enter your class: ")

# Generates a random integer between 1 and 100
random_number = random.randint(1,100)

# Formatted output using string concatenation
print()
print("Class: " + class_name)
print("Random Number: ", + random_number)