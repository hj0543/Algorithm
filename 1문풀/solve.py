import sys
sys.stdin = open('input.txt', 'r')

# 2628
import sys
input = sys.stdin.readline

W, H = map(int, input().split()) # 10 8

N = int(input()) # 3


# 분기점 설정
vert = [0, W] # [0, 10, 4]

hori = [0, H] # [0, 8, 3, 2]

# 분기점 구해서 리스트에 넣기
for _ in range(N):
    a, b = map(int, input().split())
    
    if a != 0:
        vert.append(b)
    else:
        hori.append(b)

# 분기점 오름차순 정렬
sorted_vert = sorted(vert) # [0, 4, 10]
sorted_hori = sorted(hori) # [0, 2, 3, 8]

# 나눠진 가로, 세로의 길이
width = [] # [4, 6]
height = [] # [2, 1, 5]

# 분기점을 기준으로 가로, 세로 나눈기
for i in range(1, len(sorted_vert)):
    w = sorted_vert[i] - sorted_vert[i-1]
    width.append(w)

for j in range(1, len(sorted_hori)):
    h = sorted_hori[j] - sorted_hori[j-1]
    height.append(h)    

# 가로의 최댓값 * 세로의 최댓값
print(max(width) * max(height))
