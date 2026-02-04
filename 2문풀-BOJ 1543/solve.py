import sys
sys.stdin = open('input.txt', 'r')

# 1543
import sys
input = sys.stdin.readline

A = list(map(str, input().rstrip()))
B = list(map(str, input().rstrip()))
# -> 공백으로 나올 수도 있고 공백으로 안나올 수도 있음


# 범위 넘어가면 패스하는 로직 추가 필요
length_B = len(B)
total = 0
for i in range(0, len(A), length_B):
    cnt = 0
    for j in range(length_B):
        if A[i+j] == B[j]:
            cnt += 1
    if cnt == length_B:
        total += 1

print(total)