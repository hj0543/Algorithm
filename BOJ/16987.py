# [로직설계]
# 

# 1. 



import sys
input = sys.stdin.readline

def func():
    pass

# --------------------------------------------------------

N = int(input())

eggs = []   # (계란의 내구도, 무게)
for _ in range(N):
    eggs.append(tuple(map(int, input().split())))

print(eggs)