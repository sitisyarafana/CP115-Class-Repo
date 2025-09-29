score1 = int(input("Enter test score 1: "))
score2 = int(input("Enter test score 2: "))
score3 = int(input("Enter test score 3: "))

# Calculates the total score and average score
total_score = score1 + score2 + score3
average_score = total_score / 3

# Displays all individual scores, total, and average
print(f"Test score 1 = {score1}")
print(f"Test score 2 = {score2}")
print(f"Test score 3 = {score3}")
print(f"Total Score = {total_score}")
print(f"Average Score = {average_score}")