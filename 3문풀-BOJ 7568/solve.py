import sys
sys.stdin = open('input.txt', 'r')

# 7568
import sys
input = sys.stdin.readline


TC = int(input())

rank = [0] * TC
data = []
for i in range(TC):
    WH = list(map(int, input().split()))
    data.append(WH)

for i in range(len(data)):
    for j in range(len(data)):
if WH[0] > WH[i]:
        rank[i]

print(len(data))