import sys
input = sys.stdin.readline

def arithmetic_sequence(a, b):
    low = max(0, b-a)
    high = b
    count = high - low + 1
    total_sum = (low + high) * count // 2
    return total_sum

T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    print(arithmetic_sequence(K, N)*4)