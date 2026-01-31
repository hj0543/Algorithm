import sys
input = sys.stdin.readline

minutes = list(map(int, input().split())) # 2 2 3 3
times = list(map(int, input().split())) # 1 3 4

A = int(minutes[0])
B = int(minutes[1])
C = int(minutes[2])
D = int(minutes[3])

# 개가 공격적이고 쉬는 타임을 나타내는 리스트 -> 1:공격적, 0:쉼
D1 = [] # [1, 1, 1, 0, 0, 1, 1, 1, 0]
D2 = [] # [1, 1, 1, 1, 1, 0, 0, 0, 0]


# D1 에 넣을 값 반복문
for i in range(1, max(times) + 1):
    if 0 < i % (A + B) <= A: # i를 5로 나누었을때 나머지가 0초과 2이하라면
        D1.append(1) # 공격적인 표시를 더한다.
    else:
        D1.append(0)

# D2 에 넣을 값 반복문
for i in range(1, max(times) + 1):
    if 0 < i % (C + D) <= C: # i를 9으로 나누었을때 나머지가 0초과 4이하라면
        D2.append(1) # 공격적인 표시를 더한다.
    else:
        D2.append(0)
#
# print(D1)
# print(D2)

for j in range(len(times)):
    cnt = 0

    # for k in range(len(times)):
    if D1[int(times[j])-1] == 1:
        cnt += 1
    if D2[int(times[j])-1] == 1:
        cnt += 1
    print(cnt)