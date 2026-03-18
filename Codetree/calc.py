
arr = [6,3,2,7,8,11,10,9]

avg = sum(arr) / len(arr)

boonsan = []
for i in range(len(arr)):
    boonsan.append((arr[i] - avg) ** 2)

result = (sum(boonsan) / len(arr)) ** 0.5

print(result)