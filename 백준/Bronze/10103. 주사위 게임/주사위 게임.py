import sys
input = sys.stdin.readline

n = int(input())

total_a = 100
total_b = 100

for _ in range(n):
    scores = list(map(int, input().split()))


    if scores[0] > scores[1]:
        total_b -= scores[0]
    elif scores[0] < scores[1]:
        total_a -= scores[1]
    else:
        pass
    
print(total_a)
print(total_b)