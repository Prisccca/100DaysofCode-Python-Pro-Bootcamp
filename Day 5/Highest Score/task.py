student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
total_exam = sum(student_scores)
print(total_exam)

som = 0
for score in student_scores:
    som += score
print(som)

greaterthan = student_scores[0]
for score in range(1,len(student_scores)):
    if student_scores[score] > greaterthan:
        greaterthan = student_scores[score]

print(greaterthan)

print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)