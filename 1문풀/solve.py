import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

list_number = list(N)

result_list = []
# while x < 10:

for i in range(10): # i => list_number[0]
    for j in range(10): # j => list_number[1]
        for k in range(10):
            if 101 * i + 11 * j + 2 * k == N:
                result = 100 * i + 10 * j + k
                result_list.append(result)
### 이러면 3자리만 되는구나
# 생성자가 없으면 0을 출력해야됨.

print(min(result_list))



    # N = 101 * a + 11 * b + 2 * c # N = 100 * a + 10 * b + c + a + b + c
    # result = 100 * a + 10 * b + c
