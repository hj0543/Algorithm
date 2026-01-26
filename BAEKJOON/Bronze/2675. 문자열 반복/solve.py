import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(T):
    R, S = map(str, input().split())
    num_R = int(R)
    result = []
    for word in S:
        result.append(word * num_R)
    res = ''.join(result)
    print(res)