import sys
import heapq

input = sys.stdin.readline


def clean_max_heap():
    # 이미 solved 되었거나, 더 최신 add로 덮인 오래된 정보는 제거
    while max_heap:
        neg_level, neg_problem = max_heap[0]
        level = -neg_level
        problem = -neg_problem

        if level_of.get(problem) == level:
            return
        heapq.heappop(max_heap)


def clean_min_heap():
    # min_heap도 같은 방식으로 현재 유효한 정보만 남긴다
    while min_heap:
        level, problem = min_heap[0]

        if level_of.get(problem) == level:
            return
        heapq.heappop(min_heap)


n = int(input())

# problem -> current level
level_of = {}

# 최대 난이도 추천용: 난이도 내림차순, 문제 번호 내림차순
max_heap = []

# 최소 난이도 추천용: 난이도 오름차순, 문제 번호 오름차순
min_heap = []

for _ in range(n):
    problem, level = map(int, input().split())
    level_of[problem] = level
    heapq.heappush(max_heap, (-level, -problem))
    heapq.heappush(min_heap, (level, problem))

m = int(input())

for _ in range(m):
    command = input().split()

    if command[0] == "add":
        problem = int(command[1])
        level = int(command[2])

        # 새 문제를 추가하거나, 기존 문제의 난이도를 갱신
        level_of[problem] = level
        heapq.heappush(max_heap, (-level, -problem))
        heapq.heappush(min_heap, (level, problem))

    elif command[0] == "solved":
        problem = int(command[1])

        # 힙에서 바로 삭제하지 않고 현재 유효 목록에서만 제거
        del level_of[problem]

    else:
        option = int(command[1])

        if option == 1:
            # top이 오래된 정보일 수 있으므로 먼저 정리
            clean_max_heap()
            print(-max_heap[0][1])
        else:
            clean_min_heap()
            print(min_heap[0][1])
