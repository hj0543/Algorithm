import sys
input = sys.stdin.readline

S, P = map(int, input().split()) # 9 8

words = list(input().rstrip()) # CCTGGATTG

need = list(map(int, input().split())) # 2 0 1 1

# 현재 윈도우 A, C, G, T 개수
cur = [0, 0, 0, 0]

# 초기 윈도우 설정
for i in range(P):
    if words[i] == 'A':
        cur[0] += 1
    elif words[i] == 'C':
        cur[1] += 1
    elif words[i] == 'G':
        cur[2] += 1
    elif words[i] == 'T':
        cur[3] += 1

#################################################################

def cond():
    for i in range(4):
        if cur[i] < need[i]:
            return False
    return True

#################################################################

cnt = 0

# 초기환경 조건 만족하면 +1
if cond():
    cnt += 1

for i in range(P, S):

    # 왼쪽에 문자는 빠져나가기
    left = words[i - P]
    if left == 'A':
        cur[0] -= 1
    if left == 'C':
        cur[1] -= 1
    if left == 'G':
        cur[2] -= 1
    if left == 'T':
        cur[3] -= 1


    # 오른쪽에 문자는 더하기
    right = words[i]
    if right == 'A':
        cur[0] += 1
    if right == 'C':
        cur[1] += 1
    if right == 'G':
        cur[2] += 1
    if right == 'T':
        cur[3] += 1

    # 조건 만족하면 +1
    if cond():
        cnt += 1

print(cnt)