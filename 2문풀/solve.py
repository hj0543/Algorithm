import sys
sys.stdin = open('input.txt', 'r')

# 1448
import sys
input = sys.stdin.readline
N = int(input())

length = [] # 빨대의 길이 리스트
for _ in range(N):
    T = int(input())
    length.append(T)


'''
가장 긴 것 3개가 안되면 짧은거 3개라도 해봐야함.. 이 부분 수정필요
'''

sort_length = sorted(length) # 정렬해서 TOP3 뽑아내기 위해
if sort_length[-1] < sort_length[-2] + sort_length[-3]: # 삼각형이 만들어지는 조건
    print(sum(sort_length[-3:])) # 가장 긴 변의 길이 3개 합
else:
    print(-1) # 만약 삼각형을 만들 수 없으면 -1을 출력한다.

