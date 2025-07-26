total = 0.0
sum = 0.0

for _ in range(20):
    subject, score, grade = map(str, input().split())
    score = float(score)
    num = 0.0
    if grade == 'P':
        continue

    if grade == 'A+':
        num = 4.5
    elif grade == 'A0':
        num = 4.0
    elif grade == 'B+':
        num = 3.5
    elif grade == 'B0':
        num = 3.0
    elif grade == 'C+':
        num = 2.5
    elif grade == 'C0':
        num = 2.0
    elif grade == 'D+':
        num = 1.5
    elif grade == 'D0':
        num = 1.0
    elif grade == 'F':
        num = 0.0

    sum += score * num
    total += score

print(sum / total)