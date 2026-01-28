import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for _ in range(T):
    init = list(map(int, input().split()))

##############################################################

x1 = []
y1 = []


for i in range(init[0]):
    for j in range(init[1]):            
        rang = (i - init[0] ** 2 + j - init[1] ** 2) ** 0.5
        if rang <= init[2]:

        













