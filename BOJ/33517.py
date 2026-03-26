import sys
input = sys.stdin.readline

# 입력부
N = int(input())
stepping_stones = list(map(int, input().split()))
K = int(input())
commands = input().strip()

# ---------------------------------------------------------------

times = 0
for i in range(N):
    if stepping_stones[i] == 0:
        times += 1
    elif stepping_stones[i] == -1:
        times += 2
    else:
        times += (stepping_stones[i] + 1)


recur_commands = ''
for i in range(times):
    recur_commands += commands

# print(recur_commands)

idx = 0
for cmd in recur_commands:
    if idx == N:
        print('YES')
        exit()

    # J -> 빈 칸이면 이동
    if cmd == 'J':
        if stepping_stones[idx+1] == 0:
            idx += 1
        
            continue

    # A -> 앞에 곰이 있다면 곰의 체력을 -1, 지뢰가 있다면 게임종료     
    elif cmd == 'A':
        if stepping_stones[idx+1] >= 1:
            stepping_stones[idx+1] -= 1
            continue
        elif stepping_stones[idx+1] == -1:
            print('NO')
            exit()

    # D -> 앞에 지뢰가 있다면 지뢰제거
    elif cmd == 'D':
        if stepping_stones[idx+1] == -1:
            stepping_stones[idx+1] = 0

if idx == N:
    print('YES')
else:
    print('NO')

