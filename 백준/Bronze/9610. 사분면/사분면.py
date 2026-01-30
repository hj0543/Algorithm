import sys
input = sys.stdin.readline

n = int(input())

coordinate = []


for _ in range(n):
    nums = input().split()
    coordinate.append(nums)

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for i in range(n):

    x = int(coordinate[i][0])
    y = int(coordinate[i][1])
    
    if x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1
    else:
        AXIS += 1
    
print(f'Q1: {Q1}', f'Q2: {Q2}', f'Q3: {Q3}', f'Q4: {Q4}', f'AXIS: {AXIS}', sep = '\n')