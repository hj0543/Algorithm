import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

total = 0

for i in range(1, 10): # 문제를 잘 읽읍시다...
    for j in range(1, 10):
        if N == (i * j):
            total += 1        
if total != 0:
    print('1')
else:
    print('0')
# if(total) == 0:
#     print(0)
# else:
#     print(1)