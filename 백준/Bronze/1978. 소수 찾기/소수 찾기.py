N = int(input())

nums = list(map(int, input().split()))


total = 0
for i in nums:
    if i == 1:
        continue
    
    is_prime = True
    for j in range(2, i // 2 + 1): # 반값까지 나눠지는 수 없으면 더 이상 약수 없음
        if i % j == 0:
            is_prime = False # 나눠지는 수가 있으면 소수가 아니다
            break
    if is_prime: # 나눠지는 수가 없으면 소수이다.
        total += 1 # 갯수 1개 추가
            
print(total)