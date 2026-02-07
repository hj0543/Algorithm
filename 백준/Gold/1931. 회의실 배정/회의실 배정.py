import sys
input = sys.stdin.readline

N = int(input())
conf = []
for _ in range(N):
    conf.append(list(map(int, input().split())))

conf.sort(key=lambda x: (x[1], x[0]))

# print(conf) # [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

time = []
time.append(conf[0]) # [1, 4]

cnt = 0
for i in range(1, N):
    if conf[i][0] >= time[cnt][1]:
        time.append(conf[i])
        cnt += 1

print(len(time))