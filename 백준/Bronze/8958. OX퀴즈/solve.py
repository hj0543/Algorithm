import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for _ in range(1, N + 1):
    OX = list(input())

    total_score = 0
    current_score = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            current_score += 1
            total_score += current_score
        else:
            current_score = 0
    
    print(total_score)