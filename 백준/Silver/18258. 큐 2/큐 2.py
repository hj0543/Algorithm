import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))

    elif cmd[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())

    elif cmd[0] == 'size':
        print(len(queue))

    elif cmd[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif cmd[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)