nums = []

for i in range(2, 10):
    for j in range(1, 10):
        value = (i * j)

        nums.append(value)

slice_nums = []
result = []

for n in range(0, len(nums), 9):
    slice_nums = nums[n : (n + 9)]

    result.append(slice_nums)

for x in range(len(result)):
    for y in range(len(result[x])):
        if result[x][y] % 3 == 0 or result[x][y] % 7 == 0:
            del result[x][y]

print(result)

        