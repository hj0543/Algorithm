A, B, C = map(int, input().split())

D = int(input())

total = A * 3600 + B * 60 + C + D

H = (total // 3600) % 24
M = ((total % 3600) // 60) % 60
S = (total % 3600) % 60

print(H, M, S, sep = ' ')