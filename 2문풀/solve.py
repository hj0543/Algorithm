import sys
sys.stdin = open('input.txt', 'r')

# 22864
import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

# 시간, 피로도, 일의 양 초기값 설정
hour = 0
fatigue = 0
work = 0

while hour < 24: # 24시간 동안

    if fatigue + A <= M: # 현재 피로도에서 더할 피로도가 최대한계 이하라면
        fatigue += A # 일해야지
        work += B
        hour += 1
    else: # 이하가 아니라면
        fatigue -= C # 쉬어야지
        if fatigue < 0:
            fatigue = 0
        hour += 1

print(work)







