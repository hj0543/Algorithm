import sys
input = sys.stdin.readline
N = int(input())

total = []

for _ in range(N):
    numbers = list(map(int,input().split()))
    
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]



    if a == b == c: # 3개 다 같은 눈이 나올 경우
        result = 10000 + a * 1000
    elif a != b != c != a: # 3개 다 다른 눈이 나올 경우 # a != b != c 하면 틀림
        result = max(numbers) * 100
    else: # 2개만 같은 눈이 나올 경우
        if a == b:
            result = 1000 + a * 100
        elif c == b:
            result = 1000 + b * 100
        else:
            result = 1000 + c * 100
    
    
    total.append(result) # 나온 값들을 total 리스트에 담고
    
print(max(total)) # 최댓값 출력