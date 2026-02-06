import sys
sys.stdin = open('input.txt', 'r')

# 과제풀이용
import sys
input = sys.stdin.readline

import sys
def solve():
    # 입력 처리
    N, A = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    start_pos = (x1 - 1, y1 - 1)
    target_pos = (x2 - 1, y2 - 1)

    # 현재 코디가 있을 수 있는 위치들의 집합
    current_positions = {start_pos}

    # 방문 체크 (무한 루프 방지용: 좌표 + 시간주기)
    # 3차원 배열 대신 set으로 방문 처리를 간단하게 관리
    visited_states = set()
    visited_states.add((start_pos[0], start_pos[1], 0))

    time = 0
    # 주기는 3 * A (O -> G -> R)
    period = 3 * A

    while current_positions:
        if target_pos in current_positions:
            print(time)
            return

        next_positions = set()
        next_time = time + 1
        current_mod = next_time % period  # 다음 턴의 나머지

        # 현재 가능한 모든 위치에서 확산
        for r, c in current_positions:
            # 5가지 행동: 상, 하, 좌, 우, 제자리(대기)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                nr, nc = r + dr, c + dc

                # 격자 범위 체크
                if 0 <= nr < N and 0 <= nc < N:
                    # --- 핵심: 다음 턴에 이 칸이 'G'인지 확인 ---
                    # 초기 상태값: 0(R), 1(O), 2(G)
                    initial_color = grid[nr][nc]

                    # 1. 초기색이 R(0)이거나 G(2)인 경우: 색이 안 변함
                    if initial_color != 1:
                        # 이동하려는 곳이 G여야 함 (R이면 못감)
                        if initial_color == 2:
                            if (nr, nc, current_mod) not in visited_states:
                                visited_states.add((nr, nc, current_mod))
                                next_positions.add((nr, nc))

                    # 2. 초기색이 O(1)인 경우: 주기적으로 변함
                    else:
                        # 변하는 순서: O(1) -> G -> R -> O ...
                        # A턴 동안 유지됨.
                        # cycle_idx: 0(O), 1(G), 2(R) 중 무엇인가?
                        cycle_idx = (next_time // A) % 3

                        # 우리가 원하는 건 G 상태일 때 (cycle_idx가 1일 때)
                        if cycle_idx == 1:
                            if (nr, nc, current_mod) not in visited_states:
                                visited_states.add((nr, nc, current_mod))
                                next_positions.add((nr, nc))

        current_positions = next_positions
        time += 1

        # (선택) 너무 오래 걸리면 탈출 (안전장치)
        if time > 100000:  # 적절한 상한선
            break

    print(-1)


solve()

