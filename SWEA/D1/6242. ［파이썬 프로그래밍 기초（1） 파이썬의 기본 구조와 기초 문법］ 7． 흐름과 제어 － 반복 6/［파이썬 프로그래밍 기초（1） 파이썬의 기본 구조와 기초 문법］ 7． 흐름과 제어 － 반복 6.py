blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
counts = {}

for bt in blood_type:

    counts[bt] = counts.get(bt, 0) + 1

print(counts)