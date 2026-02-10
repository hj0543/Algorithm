import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    count = 0
    
    for last in range(N - 1, 0, -1):
        for i in range(last):
            if A[i] > A[i+1]:
                # 교환
                A[i], A[i+1] = A[i+1], A[i]
                count += 1
                
                if count == K:
                    print(*A)
                    return

    print(-1)

if __name__ == "__main__":
    solve()