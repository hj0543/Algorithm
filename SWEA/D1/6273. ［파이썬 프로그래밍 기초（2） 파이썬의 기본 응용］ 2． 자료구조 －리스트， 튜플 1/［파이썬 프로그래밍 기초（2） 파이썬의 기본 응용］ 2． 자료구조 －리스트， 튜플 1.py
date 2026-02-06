student = ((90, 80), (85, 75), (90, 100))

for n in range(0, 3):
    sum_score = student[n][0] + student[n][-1]
    avg_score = sum_score / len(student[0])
    print(f'{n + 1}번 학생의 총점은 {sum_score}점이고, 평균은 {avg_score}입니다.')