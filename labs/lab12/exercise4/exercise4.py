passing_count = 0
failing_count = 0
total_score  = 0

score_input = input()

# TODO: Your code here
while score_input.lower() != "end" :
    score = int(score_input)

if score >= 60:
        passing_count += 1
else: 
        failing_count += 1
total_score += 1
score_input = input()

if total_score > 0:
    pass_rate = (passing_count / total_score) * 100
else:
    pass_rate = 0.0


print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
