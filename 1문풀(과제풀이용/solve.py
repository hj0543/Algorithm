import sys
sys.stdin = open('input.txt', 'r')

##################################################

def my_len(arr):
    cnt = 0
    for _ in arr:
        cnt += 1
    return cnt

T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()

    # B를 한 글자짜리 특수문자로 치환 -> replace도 쓰면 안되나,,?
    result = A.replace(B, '*')

    print(f"#{tc} {my_len(result)}")