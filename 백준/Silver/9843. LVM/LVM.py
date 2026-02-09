import sys

n = int(sys.stdin.readline())
commands = []
for _ in range(n):
    commands.append(sys.stdin.readline().split())

stack = []
register = 0
pc = 0 

while pc < n:
    cmd = commands[pc]
    op = cmd[0]

    if op == 'PUSH':
        stack.append(int(cmd[1]))
        pc += 1
    elif op == 'STORE':
        register = stack.pop()
        pc += 1
    elif op == 'LOAD':
        stack.append(register)
        pc += 1
    elif op == 'PLUS':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
        pc += 1
    elif op == 'TIMES':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
        pc += 1
    elif op == 'IFZERO':
        val = stack.pop()
        if val == 0:
            pc = int(cmd[1])
        else:
            pc += 1
    elif op == 'GOTO':
        pc = int(cmd[1])
    elif op == 'DONE':
        print(stack[-1])
        break