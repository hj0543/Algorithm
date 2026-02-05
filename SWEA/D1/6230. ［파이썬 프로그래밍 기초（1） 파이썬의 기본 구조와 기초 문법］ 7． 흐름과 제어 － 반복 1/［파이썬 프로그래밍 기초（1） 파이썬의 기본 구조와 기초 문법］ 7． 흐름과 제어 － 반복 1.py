score = {
    '1번 학생' : 88, 
    '2번 학생' : 30, 
    '3번 학생' : 61, 
    '4번 학생' : 55, 
    '5번 학생' : 95
}

students = list(score.keys())
scores = list(score.values())

for i in range(len(students)):

    if scores[i] >= 60:
        grade = '합격'
    else:
        grade = '불합격'

    print(f'{students[i]}은 {scores[i]}점으로 {grade}입니다.')
