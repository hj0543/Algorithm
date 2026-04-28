import sys
input = sys.stdin.readline


# -----------------------------------------------------------------------------------------------
# 입력부

N = int(input())
board = list(map(int, input().split()))
K = int(input())
macro = input().strip()


# 칸이 1개뿐이면 시작점이 곧 도착점이므로 항상 가능하다.
if N == 1:
    print("YES")
    exit()


# -----------------------------------------------------------------------------------------------
# 1. 보드 정보 누적

# bear_sum[i]  : 1번 칸부터 i번 칸까지 만나게 되는 곰 체력의 총합
# mine_count[i]: 1번 칸부터 i번 칸까지 만나게 되는 지뢰 개수

# 여기서 board[0]은 시작 칸이므로 실제로 처리해야 하는 칸은 1번 칸부터이다.

bear_sum = [0] * N
mine_count = [0] * N

for i in range(1, N):
    bear_sum[i] = bear_sum[i - 1]
    mine_count[i] = mine_count[i - 1]

    if board[i] == -1:
        mine_count[i] += 1
    elif board[i] > 0:
        bear_sum[i] += board[i]


# -----------------------------------------------------------------------------------------------
# 2. 매크로 1사이클 분석

# macro를 왼쪽부터 보면서:
# - 지금까지 나온 A의 개수
# - 지금까지 나온 D의 개수
# 를 세다가,
# J를 만날 때마다 "그 점프 직전까지 확보된 공격 횟수 / 지뢰 해제 횟수"를 저장한다.

attack_before_jump = []
disarm_before_jump = []

attack_count = 0
disarm_count = 0

for command in macro:
    if command == 'A':
        attack_count += 1
    elif command == 'D':
        disarm_count += 1
    elif command == 'J':
        attack_before_jump.append(attack_count)
        disarm_before_jump.append(disarm_count)


# 매크로 1사이클 전체를 끝냈을 때 얻는 총 공격 횟수 / 총 지뢰 해제 횟수
total_attack = attack_count
total_disarm = disarm_count

# 한 사이클 안에 J가 총 몇 번 있는지
jump_count = len(attack_before_jump)


# 점프가 한 번도 없는데 칸이 2개 이상이면 앞으로 이동 자체가 불가능하다.
if jump_count == 0:
    print("NO")
    exit()


# -----------------------------------------------------------------------------------------------
# 3. 각 점프가 가능한지 확인

# 시작 칸(0번 칸)에서 N-1번 점프하면 마지막 칸에 도착할 수 있으므로
# 총 N-1번의 점프가 필요하다.

# i번째 점프를 하기 직전에는
# 1번 칸부터 i번 칸까지의 곰/지뢰를 모두 처리할 수 있어야 한다.

# i번째 점프가
# - 매크로의 몇 번째 사이클에 속하는지
# - 그 사이클 안에서 몇 번째 J인지
# 를 계산하면,
# 그 점프 직전까지 누적된 A/D 횟수를 바로 구할 수 있다.

for i in range(1, N):
    # i번째 점프 이전에 완전히 끝난 매크로 사이클 수
    cycle = (i - 1) // jump_count

    # 현재 사이클 안에서 몇 번째 J를 쓰는지
    jump_index = (i - 1) % jump_count

    # 완전히 끝난 사이클들에서 얻은 능력치
    # + 현재 사이클에서 이번 J 직전까지 얻은 능력치
    attack_ready = cycle * total_attack + attack_before_jump[jump_index]
    disarm_ready = cycle * total_disarm + disarm_before_jump[jump_index]

    # i번째 칸까지 오기 위해 필요한 총 공격량 / 총 지뢰 해제 횟수
    need_attack = bear_sum[i]
    need_disarm = mine_count[i]

    # 하나라도 부족하면 이 점프를 할 수 없으므로 실패
    if attack_ready < need_attack or disarm_ready < need_disarm:
        print("NO")
        exit()


# 모든 점프를 문제 없이 할 수 있으면 마지막 칸까지 도달 가능
print("YES")
