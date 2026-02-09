import sys

line = sys.stdin.readline().rstrip()
stack = []
total_pieces = 0

for i in range(len(line)):
    if line[i] == '(':
        stack.append('(')
    else:
        stack.pop()

        if line[i - 1] == '(':
            total_pieces += len(stack)
        else:
            total_pieces += 1

print(total_pieces)