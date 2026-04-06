import sys
sys.stdin = open('input.txt', 'r')

##################################################
# SWEA [PRO] 타워디펜스게임

# [문제요약]
# 1. S는 출발지, E는 도착지 (경로는 유일함이 보장된다.)
# 2. 각 타워는 재장전시간을 가진다. 한 번 공격 후 재장전시간이 지나야 다시 공격할 수 있다.
# 3. 모든 타워는 공격범위가 3이다. (상, 하, 좌, 우 합 총 3칸 - 범위공격)
# 4. 도망자는 매 행동주기마다 순차적으로 출발지에서 나타나며, 도착지까지 1칸씩 이동하여 도착지에 도착하는 즉시 맵에서 사라진다.

# [타워의 공격 대상 선정 방법]
# 1. 공격준비가 되지 않은 타워는 공격할 대상을 찾지 않는다.
# 2. 공격준비가 된 타워는 공격할 대상을 찾는다.
# 공격준비가 되었다는 말의 의미는, 마지막 공격 후 재장전 시간이 지났음을 의미한다.
# 2-a. 가장 마지막에 공격했던 대상이 살아 있고 그것이 사정거리내에 있다면, 공격대상을 유지한다.
# (주의 : 마지막에 공격했던 대상이 공격 준비가 안되었을 때 잠깐 사정거리에서 벗어났더라도 현재 사정거리내에 존재한다면, 공격대상을 바꾸지 않고 그것을 공격대상으로 선정한다.)
# 2-b. 그렇지 않을 경우 새로운 대상을 찾는다.
# 2-c. 새로운 대상은 다음과 같은 우선순위를 기준으로 선정한다.
# 우선순위 1. 사정거리 내에 있는 대상
# 우선순위 2. (우선순위 1 에 해당하는 도망자들이 둘 이상일 경우) 그 중 남은 체력이 가장 적은 대상.
# 우선순위 3. (우선순위 2 에 해당하는 도망자들이 둘 이상일 경우) 그 중 맵에 먼저 나타난 대상
# 3. 공격대상을 선정하지 못한 타워는 다음 턴에 다시 공격대상을 찾는다. 이 경우 마지막 공격대상이 없는 상태가 된다.

# [도망자의 체력]
# 도망자는 체력 값을 가지고 있다.
# 모든 도망자는 같은 체력 값을 가지고 시작한다.
# 체력은 타워로부터 공격 당할때마다 1씩 감소하며, 체력이 0 이 된 도망자는 사망하여 맵에서 즉시 사라진다.

# [정리]
# 매 턴 발생하는 상황을 전체적으로 정리하면 다음과 같다.
# 1. 공격 준비가 안된 타워들은 아무 행동도 하지 않고 턴을 종료한다.
# 2. 공격 준비가 된 타워들은 공격 대상을 선택한다.
# 3. 공격 대상을 선택하지 못한 타워는 직전 공격대상이 없는 상태가 된다. 턴을 종료 한다.
# 4. 공격 준비가 된 모든 타워들은 동시에 지정한 타겟을 공격한다.
# 이 때 도망자의 남은 체력보다 더 많은 공격이 들어갈 수 있음에 유의하라.
# 5. 도망자들은 공격을 받은 만큼 체력이 감소한다.
# 6. 체력이 0 이 된 도망자는 사망하여 맵에서 사라진다.
# 7. (현재 턴에 행동주기가 도래했다면) 도망자들은 1 칸씩 도착지를 향해 이동한다.
# 아직 남아있는 도망자가 있다면 출발지에 새로운 도망자가 나타난다.
# 도착지에 도착한 사망자는 맵에서 사라진다. 

# 마지막으로 모든 도망자가 탈출했거나 죽었을 경우 게임이 종료된다.


from typing import List

# Global variables to store game state
_N = 0
_mMap = []
_path = [] # List of (r, c) tuples representing the path from S to E
_towers = [] # List of tower objects/dicts
_start_pos = (0, 0)
_end_pos = (0, 0)

# Helper function to calculate Manhattan distance
def manhattan_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

# Helper function to find path using BFS
def find_path(N, mMap, start_pos, end_pos):
    q = [(start_pos, [start_pos])] # (current_pos, current_path)
    visited = {start_pos}
    
    dr = [-1, 1, 0, 0] # Up, Down, Left, Right
    dc = [0, 0, -1, 1]

    while q:
        (r, c), current_path = q.pop(0)

        if (r, c) == end_pos:
            return current_path

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                # Path cells are 1, start is 2, end is 3.
                # We can move through 1, 2, 3.
                if mMap[nr][nc] in [1, 2, 3]:
                    visited.add((nr, nc))
                    q.append(((nr, nc), current_path + [(nr, nc)]))
    return [] # Should not happen based on problem statement (path guaranteed)

# 테스트 케이스에 대한 초기화 함수
# N : 맵의 크기, mMap : 맵의 각 셀의 정보
def init(N : int, mMap : List[List[int]]) -> None:
    global _N, _mMap, _path, _towers, _start_pos, _end_pos
    _N = N
    _mMap = [row[:] for row in mMap] # Deep copy
    _towers = [] # Reset towers for new test case
    _path = [] # Reset path for new test case

    # Find start (2) and end (3) positions
    for r in range(N):
        for c in range(N):
            if _mMap[r][c] == 2:
                _start_pos = (r, c)
            elif _mMap[r][c] == 3:
                _end_pos = (r, c)
    
    _path = find_path(_N, _mMap, _start_pos, _end_pos)

# 새로운 타워가 추가되는 함수
# mRow, mCol : 타워의 위치, mInterval : 타워의 재장전 시간
def addTower(mRow : int, mCol : int, mInterval : int) -> None:
    global _towers
    _towers.append({
        'r': mRow,
        'c': mCol,
        'interval': mInterval,
        'last_attack_turn': -mInterval, # To be ready on turn 0
        'target_fugitive_idx': -1 # No target initially
    })
# 시뮬레이션 실행 함수
# M : 도망자의 수, mInterval : 도망자의 행동주기, mHP : 도망자의 체력
# mRetTs : M명 도망자들이 죽거나 탈출한 턴을 저장할 배열, mRetHP : 도망자들의 남은 체력을 저장할 배열
def runSimulation(M : int, mInterval : int, mHP : int, mRetTs : List[int], mRetHP : List[int]) -> None:
    global _towers, _path

    _fugitives = [] # List of fugitive objects/dicts for the current simulation
    
    current_turn = 0
    spawned_fugitive_count = 0
    fugitives_processed_count = 0 # Count of fugitives that are dead or escaped

    # Initialize mRetTs and mRetHP with default values (e.g., -1 for not processed)
    for i in range(M):
        mRetTs[i] = -1
        mRetHP[i] = -1

    while fugitives_processed_count < M or spawned_fugitive_count < M: # Continue until all M fugitives are spawned AND processed
        
        # 1. Tower Actions (Determine attacks)
        # Store attacks: {fugitive_idx: total_damage_this_turn}
        attacks_this_turn = {} 
        
        for tower in _towers:
            if current_turn - tower['last_attack_turn'] < tower['interval']:
                # Tower not ready
                continue

            # Tower is ready
            target_fugitive_idx = tower['target_fugitive_idx']
            
            # Check if previous target is still valid (alive and in range)
            if target_fugitive_idx != -1 and \
               target_fugitive_idx < len(_fugitives) and \
               _fugitives[target_fugitive_idx]['status'] == 'alive':
                
                target_fugitive = _fugitives[target_fugitive_idx]
                target_r, target_c = _path[target_fugitive['path_idx']]
                
                if manhattan_distance(tower['r'], tower['c'], target_r, target_c) <= 3:
                    # Keep existing target
                    attacks_this_turn[target_fugitive_idx] = attacks_this_turn.get(target_fugitive_idx, 0) + 1
                    tower['last_attack_turn'] = current_turn
                    continue # Tower attacked, move to next tower

            # If previous target invalid or no target, find a new one
            possible_targets_for_tower = [] # (fugitive_hp, fugitive_spawn_turn, fugitive_idx)
            for f_idx, fugitive in enumerate(_fugitives):
                if fugitive['status'] == 'alive':
                    f_r, f_c = _path[fugitive['path_idx']]
                    if manhattan_distance(tower['r'], tower['c'], f_r, f_c) <= 3:
                        possible_targets_for_tower.append((fugitive['hp'], fugitive['spawn_turn'], f_idx))
            
            if possible_targets_for_tower:
                # Sort by priority: lowest HP, then earliest spawn_turn
                possible_targets_for_tower.sort() # Python sorts tuples lexicographically
                
                chosen_f_idx = possible_targets_for_tower[0][2]
                tower['target_fugitive_idx'] = chosen_f_idx
                attacks_this_turn[chosen_f_idx] = attacks_this_turn.get(chosen_f_idx, 0) + 1
                tower['last_attack_turn'] = current_turn
            else:
                # No target found for this tower
                tower['target_fugitive_idx'] = -1

        # 2. Apply Damage
        for f_idx, damage in attacks_this_turn.items():
            fugitive = _fugitives[f_idx]
            if fugitive['status'] == 'alive': # Ensure it's still alive before applying damage
                fugitive['hp'] -= damage
                if fugitive['hp'] <= 0:
                    fugitive['status'] = 'dead'
                    mRetTs[fugitive['ret_idx']] = current_turn
                    mRetHP[fugitive['ret_idx']] = 0
                    fugitives_processed_count += 1

        # 3. Fugitive Movement and Spawning
        if current_turn % mInterval == 0:
            # Move existing fugitives
            for f_idx, fugitive in enumerate(_fugitives):
                if fugitive['status'] == 'alive':
                    if fugitive['path_idx'] < len(_path) - 1:
                        fugitive['path_idx'] += 1
                    
                    if fugitive['path_idx'] == len(_path) - 1: # Reached end
                        fugitive['status'] = 'escaped'
                        mRetTs[fugitive['ret_idx']] = current_turn
                        mRetHP[fugitive['ret_idx']] = fugitive['hp']
                        fugitives_processed_count += 1
            
            # Spawn new fugitive
            if spawned_fugitive_count < M:
                _fugitives.append({
                    'path_idx': 0, # Start at the beginning of the path
                    'hp': mHP,
                    'spawn_turn': current_turn,
                    'status': 'alive',
                    'ret_idx': spawned_fugitive_count # Index for mRetTs/mRetHP
                })
                spawned_fugitive_count += 1
        
        # Check if all fugitives are processed and spawned
        if fugitives_processed_count == M and spawned_fugitive_count == M:
            break
        
        current_turn += 1
