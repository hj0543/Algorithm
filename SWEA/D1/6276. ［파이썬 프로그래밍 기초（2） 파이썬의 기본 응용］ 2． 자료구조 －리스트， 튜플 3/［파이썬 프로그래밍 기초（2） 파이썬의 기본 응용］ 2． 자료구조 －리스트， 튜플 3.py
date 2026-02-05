result = []
can = []

for i in range(2, 10):
    row = [] 
    for j in range(1, 10):
        value = (i * j)
        if value % 3 == 0 or value % 7 == 0:
            can.append(value)
        else:
            row.append(value)
    result.append(row)

print(result)

        