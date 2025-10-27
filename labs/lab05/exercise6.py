# Takes time in minutes from the user
minutes = int(input("Enter time in minutes : "))

# Converts minutes to hours and remaining minutes
hours = minutes // 60
remaining_minutes = minutes % 60

# Displays the original minutes and converted time format
print(f"Original minutes = {minutes}")
print(f"Converted time format = {hours}")
print(f"Converted time format = {remaining_minutes}")