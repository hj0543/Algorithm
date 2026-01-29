import sys
sys.stdin = open('input.txt', 'r')

<<<<<<< HEAD
# 42476
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(1)
    sys.exit()


cnt1 = []
cnt2 = []
total = 0



for i in range(1, n):
    if nums[i] <= nums[i - 1]:
        total += 1
    else:
        cnt1.append(total)
        total = 0
cnt1.append(total)

total = 0

for i in range(1, n):
    if nums[i] >= nums[i - 1]:
        total += 1
    else:
        cnt2.append(total)
        total = 0
cnt2.append(total)    

result1 = max(cnt1)
result2 = max(cnt2)


if result1 >= result2:
    print(result1 + 1)

else:
    print(result2 + 1)


=======
# 4948
import sys
input = sys.stdin.readline

##################################################################

import math

def is_prime(n):
    if n < 2:
        return False
    # 2부터 n의 제곱근까지 나누어 봄
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False # 소수가 아님
    return True # 소수임

########################################################################

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0 # 소수의 개수 초기값 0 설정


    for i in range(n + 1, (2 * n) + 1): # n초과 2n미만의 범위에서
        if is_prime(i) == True: # i가 소수라면
            cnt += 1 # 카운트를 한다.
        else: # 아니면 패스
            pass


    print(cnt)


    

>>>>>>> 957084cac80be7a80082671b0e152febb4160ddf
