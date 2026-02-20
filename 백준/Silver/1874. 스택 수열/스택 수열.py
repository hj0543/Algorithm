n = int(input())

sequence = []
for _ in range(n):
    sequence.append(int(input()))

stack = []
counts = 1
i = 0
result = []
while len(result) <= n*2:
    if not stack or sequence[i] != stack[-1]:
        stack.append(counts)
        result.append('+')
        counts += 1
    elif sequence[i] == stack[-1]:
        stack.pop()
        result.append('-')
        i += 1
    if len(result) == n*2:
        break
# print(result)
if result.count('+') == result.count('-'):
    for i in range(n*2):
        print(result[i])
else:
    print('NO')