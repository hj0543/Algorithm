import sys
input = sys.stdin.readline
from bisect import bisect_left


INF = float('inf')


# 현재 시간 now 이후에 특정 명령이 가장 먼저 나오는 절대 시간을 구하는 함수

# pos_list에는 매크로 안에서 그 명령이 등장하는 위치들이 들어 있다.
# now는 "마지막으로 사용한 명령의 절대 위치"이다.
# 따라서 다음 명령은 now + 1부터 찾기 시작해야 한다.
# 이 함수는 매크로가 무한 반복된다고 생각하고,
# now 이후에 해당 명령이 처음 등장하는 절대 위치를 반환한다.
def get_next(pos_list, now):
    # 해당 명령이 매크로에 한 번도 없으면 절대 수행할 수 없다.
    if not pos_list:
        return INF

    # 이제 now 다음 칸부터 명령을 찾아야 한다.
    target = now + 1

    # target이 매크로의 몇 번째 cycle에 속하는지 계산
    cycle = target // K

    # 그 반복 안에서 몇 번째 위치부터 찾아야 하는지 계산
    remain = target % K

    # bisect_left는 정렬된 리스트에서
    # remain 이상이 처음 나오는 위치의 인덱스를 반환한다.
    idx = bisect_left(pos_list, remain)
    
    # 현재 반복 안에서 찾을 수 있으면 그 위치를 절대 시간으로 바꿔서 반환
    if idx < len(pos_list):
        return cycle * K + pos_list[idx]

    # 현재 반복 안에서는 더 이상 없으면 다음 반복의 첫 등장 위치를 반환
    else:
        return (cycle + 1) * K + pos_list[0]


# 현재 시간 now 이후에 공격 A를 cnt번 수행했을 때,
# 마지막 공격이 실행되는 절대 시간을 구하는 함수
def get_attack_time(now, cnt):
    # A 명령이 한 번도 없으면 공격 자체가 불가능하다.
    if not a_list:
        return INF

    target = now + 1
    cycle = target // K
    remain = target % K

    # 현재 사이클에서 remain 이상인 첫 번째 A의 위치 찾기
    idx = bisect_left(a_list, remain)

    # 현재 사이클 안에서 앞으로 사용할 수 있는 A의 개수
    left_in_cycle = len(a_list) - idx

    # 필요한 공격 수가 현재 사이클 안에서 다 해결되면 바로 위치를 반환
    if cnt <= left_in_cycle:
        return cycle * K + a_list[idx + cnt - 1]

    # 현재 사이클의 A를 모두 사용해도 부족하다면 남은 공격 수를 줄인다.
    cnt -= left_in_cycle

    # 다음 사이클들에서 몇 번의 전체 사이클이 더 필요한지 계산
    # rest는 마지막 사이클에서 몇 번째 A를 쓰는지를 뜻한다.
    full, rest = divmod(cnt - 1, len(a_list))
    cycle += full + 1

    return cycle * K + a_list[rest]


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

# 매크로에서 A, D, J가 등장하는 위치를 각각 따로 저장한다.
# 속도 조금 줄어보겠다고 별 짓을 다하네
a_list = []
d_list = []
j_list = []

for i in range(K):
    if macro[i] == 'A':
        a_list.append(i)
    elif macro[i] == 'D':
        d_list.append(i)
    else:
        j_list.append(i)

# now는 지금까지 사용한 마지막 명령의 절대 위치를 뜻한다.
# 아직 아무 명령도 사용하지 않았으므로 -1에서 시작한다.
now = -1

# 2번 칸부터 N번 칸까지 순서대로 확인한다.
# board[0]은 시작 칸이므로 따로 처리할 필요가 없다.
for i in range(1, N):
    x = board[i]

    # 빈 칸이면 장애물이 없으므로 점프 J만 하면 된다.
    if x == 0:
        jump_time = get_next(j_list, now)

        # 점프가 더 이상 나오지 않으면 앞으로 갈 수 없다.
        if jump_time == INF:
            print("NO")
            exit()

        # 점프를 수행했으므로 현재 시간을 갱신
        now = jump_time

    # -1이면 지뢰 칸이다.
    # 이 경우에는 반드시 점프 전에 D가 먼저 나와야 한다.
    elif x == -1:
        d_time = get_next(d_list, now)
        a_time = get_next(a_list, now)
        j_time = get_next(j_list, now)

        # D보다 A나 J가 먼저 나오면,
        # 지뢰를 해제하기 전에 다른 행동을 하게 되므로 실패
        if d_time >= min(a_time, j_time):
            print("NO")
            exit()

        # 먼저 D를 사용해서 지뢰를 해제
        now = d_time

        # 그 다음 점프로 다음 칸으로 이동해야 한다.
        jump_time = get_next(j_list, now)
        if jump_time == INF:
            print("NO")
            exit()

        now = jump_time

    # 양수이면 곰 칸이다.
    # 곰의 체력이 x라면 A를 x번 먼저 해야 하고, 그 다음 J를 해야 한다.
    else:
        jump_time = get_next(j_list, now)
        attack_time = get_attack_time(now, x)

        # 필요한 공격을 모두 하기 전에 J가 먼저 나오면
        # 곰을 처리하지 못한 상태로 점프해야 하므로 실패
        if attack_time >= jump_time:
            print("NO")
            exit()

        # 곰을 모두 처리한 시점으로 현재 시간을 갱신
        now = attack_time

        # 이제 점프로 다음 칸으로 이동
        jump_time = get_next(j_list, now)
        if jump_time == INF:
            print("NO")
            exit()

        now = jump_time

# 모든 칸을 문제 없이 통과했다면 가능
print("YES")
