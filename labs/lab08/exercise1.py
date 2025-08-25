score1 = 85
score2 = 92.5
score3 = 78

# Calculate the average of all three scores
result = score1 + score2 + score3
finalResult = result / 3

print(f"finalResult = {finalResult} (type: {type(finalResult)})")
print(f"finalResult = {finalResult} (type: {type(int(finalResult))})")

finalResult1 = ((score1 ** 2) / score2) + (score3 % 7)
print(f"finalResult1 = {finalResult1} (type: {type(finalResult1)})")

# compare 
Score2 = int(score2)
Score1 = float(score1)
print(f"Score2 = {Score2} (type: {type(Score2)})")
print(f"Score1 = {Score1} (type: {type(Score1)})")
print(f"The results are like that because type casting forces a value to be treated as a different data type. When converting a float to an integer, the decimal is dropped, while converting an integrr to a float simply adds a.0 to the end.")