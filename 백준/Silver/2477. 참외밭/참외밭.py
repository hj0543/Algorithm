K = int(input())
data = []
for _ in range(6):
    data.append(list(map(int, input().split())))

width = []      # 가로만
height = []     # 세로만
length = []     # 길이 모두

for i in range(6):
    length.append(data[i][1])
    if data[i][0] == 1 or data[i][0] == 2:
        width.append(data[i][1])
    elif data[i][0] == 3 or data[i][0] == 4:
        height.append(data[i][1])

# 가로 세로 최대값과 최대값의 인덱스 저장
max_width = max(width)
max_width_idx = length.index(max_width)
max_height = max(height)
max_height_idx = length.index(max_height)

# (가로 최대길이 인덱스 + 3), (세로 최대길이 인덱스 + 3) --> 파인 부분의 길이가 됨
except_area = length[(length.index(max_width) + 3) % 6] * length[(length.index(max_height) + 3) % 6]

print((max_width * max_height - except_area) * K)