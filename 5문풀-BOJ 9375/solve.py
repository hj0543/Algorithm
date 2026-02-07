import sys
sys.stdin = open('input.txt', 'r')

##################################################

import sys
input = sys.stdin.readline

TC = int(input())


for tc in range(1, TC+1):
    n = int(input())
    data = {}
    # {'headgear': 2, 'eyewear': 1}
    # {'face': 3}

    for i in range(n):
        name, type = map(str, input().split())

        if type in data:
            data[type] += 1
        else:
            data[type] = 1

    # print(len(data))
    for j in data.values():
        print(j)








