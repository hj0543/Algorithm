N = int(input())                            # 스위치 개수
S = list(map(int, input().split()))         # [0, 1, 0, 1, 0, 0, 0, 1]
students = int(input())                     # 학생 수 = 2
data = []                                   # [gender, number] = [[1, 3], [2, 3]]
for i in range(students):
    data.append(list(map(int, input().split())))

for i in range(students):
    gender = data[i][0]
    number = data[i][1] - 1

    if gender == 1:                     # 남자일 때 스위치 조작
        for j in range(1, (N // (number+1)) + 1):
            if S[j * (number+1) - 1] == 1:
                S[j * (number+1) - 1] = 0
            else:
                S[j * (number+1) - 1] = 1

    else:                               # 여자일 때 스위치 조작
    # if
        if S[number] == 1:
            S[number] = 0
        else:
            S[number] = 1
        for j in range(1, number+1):
            if number + j <= N-1 and number - j >= 0:
                if S[number+j] == S[number-j]:
                    if S[number+j] == 1:
                        S[number + j], S[number-j] = 0, 0
                    else:
                        S[number + j], S[number - j] = 1, 1

                else:
                    break
            else:
                break

for i in range(0, len(S), 20):
    print(*S[i:i+20])