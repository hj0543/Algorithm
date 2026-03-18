# [로직설계]
# 

# 1. 

import sys
input = sys.stdin.readline

def func():
    pass


# --------------------------------------------------------

# n : 접시의 수 / d : 초밥의 가짓수 / k : 연속해서 먹는 접시의 수 / c : 쿠폰 번호
n, d, k, c = map(int, input().split())

sushi = []
for _ in range(n):
    sushi.append(int(input()))


