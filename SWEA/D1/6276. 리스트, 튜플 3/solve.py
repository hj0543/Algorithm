
# 삭제하는 로직 x, append를 안하는 로직으로 짬.

result = []
can = []

for i in range(2, 10):
    row = []  # ← 여기서 매 반복마다 새 리스트 생성
    for j in range(1, 10):
        value = (i * j)
        if value % 3 == 0 or value % 7 == 0:
            can.append(value)
        else:
            row.append(value)
    result.append(row)

# for n in range(0, len(nums), 9):
#     slice_nums = nums[n : (n + 9)]

#     result.append(slice_nums)

print(result)

        