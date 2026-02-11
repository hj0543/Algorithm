data = []   # [[1, 2, 4, 4], [2, 3, 5, 7], [3, 1, 6, 5], [7, 3, 8, 6]]
for i in range(4):
    data.append(list(map(int, input().split())))

grid = [[0 for _ in range(100)] for _ in range(100)]

for k in range(4):
    x1 = data[k][0]
    y1 = data[k][1]
    x2 = data[k][2]
    y2 = data[k][3]
    for i in range(x1, x2 ):
        for j in range(y1, y2 ):
            grid[i][j] = 1

total = 0
for i in range(100):
    total += sum(grid[i])

print(total)