import sys
input = sys.stdin.readline


# 현재 턴에, archer_col 열에 있는 궁수가 어떤 적을 공격할지 결정
def choose_target(attack_row, archer_col, alive):

    best_index = -1
    best_distance = d + 1
    best_col = m

    for enemy_index, (row, col) in enumerate(enemies):
        
        # 이미 죽은 적은 볼 필요가 없다.
        if not alive[enemy_index]:
            continue

        # row >= attack_row 이면 그 적은 이미 성에 도달했거나 지나간 것과 같으므로 제외
        if row >= attack_row:
            continue

        distance = (attack_row - row) + abs(archer_col - col)

        if distance > d:
            continue

        # 우선순위대로 후보를 갱신
        # 1. 더 가까우면 무조건 교체
        # 2. 거리가 같으면 더 왼쪽이면 교체
        if distance < best_distance or (distance == best_distance and col < best_col):
            best_index = enemy_index
            best_distance = distance
            best_col = col

    return best_index


# 한 가지 궁수 배치를 정했을 때의 시뮬레이션 함수
def play_game(archer_positions):

    # 각 적이 살아 있는지 확인
    alive = [True] * len(enemies)
    removed_enemy_count = 0

    # 반대로 궁수 기준 행이 올라간다고 생각
    for attack_row in range(n, 0, -1):

        # 이번 턴에 제거될 적들을 모음. 중복 타겟이 있을 수 있으므로 set 사용
        enemies_to_remove = set()

        # 목표 탐색
        for archer_col in archer_positions:
            enemy_index = choose_target(attack_row, archer_col, alive)

            # 사거리 안에 적이 있다면 제거 후보에 넣는다
            if enemy_index != -1:
                enemies_to_remove.add(enemy_index)

        # 이번 턴 공격이 끝난 뒤 한 번에 제거 처리
        for enemy_index in enemies_to_remove:
            if alive[enemy_index]:
                alive[enemy_index] = False
                removed_enemy_count += 1

    return removed_enemy_count


n, m, d = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]

# 처음 보드를 모두 확인하면서 적이 있는 칸의 좌표만 따로 저장
enemies = []
for row in range(n):
    for col in range(m):
        if castle[row][col] == 1:
            enemies.append((row, col))

result = 0

# 궁수 3명을 서로 다른 열에 놓는 모든 경우
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            result = max(result, play_game((i, j, k)))

print(result)
