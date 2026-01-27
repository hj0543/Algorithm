import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = input().strip() # list로 받으려면 int 쓰지 말 것.

arr = list(map(int, A))

total = 0

for i in range(0, N):
    total += arr[i]

print(total)

# for i in listed_A: