import sys
sys.stdin = open('input.txt', 'r')

N = list(map(float, input().split(',')))

import math
for radius in N:
    circumference = math.pi * radius * 2
    result = round(circumference, 2)

# 출력 어떻게 함...?

