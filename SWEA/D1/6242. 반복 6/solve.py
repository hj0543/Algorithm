A = 0
B = 0
AB = 0
O = 0

blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for i in blood_type:
    if i == 'A':
        A += 1
    elif i == 'B':
        B += 1
    elif i == 'AB':
        AB += 1
    else:
        O += 1

print({f'A': A, 'O': O, 'B': B, 'AB': AB})

# 실행시간 줄이는 방법(counts 이용)

'''
blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
counts = {}

for bt in blood_type:
    # 해당 혈액형이 있으면 가져오고 없으면 0을 반환하여 1을 더함
    counts[bt] = counts.get(bt, 0) + 1

print(counts)
'''