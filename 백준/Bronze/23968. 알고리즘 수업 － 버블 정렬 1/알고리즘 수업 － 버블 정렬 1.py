import sys

def solve():
    # 입력 받기
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    
    count = 0
    
    # 버블 정렬 구현 (0-based index로 변환)
    # last: 정렬될 위치 (배열의 끝에서부터 하나씩 줄어듦)
    for last in range(N - 1, 0, -1):
        for i in range(last):
            # 인접한 두 원소 비교
            if A[i] > A[i+1]:
                # 교환 (Swap)
                A[i], A[i+1] = A[i+1], A[i]
                count += 1
                
                # K번째 교환인지 확인
                if count == K:
                    # 교환된 두 수 출력 (작은 수 A[i], 큰 수 A[i+1])
                    print(f"{A[i]} {A[i+1]}")
                    return

    # K번 교환하기 전에 정렬이 끝난 경우
    print(-1)

if __name__ == "__main__":
    solve()