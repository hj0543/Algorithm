import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deque = deque()

for i in range(n):
    cmd = input().split()
    # print(cmd[0])
    if cmd[0] == '1':
        deque.appendleft(cmd[1])

    elif cmd[0] == '2':
        deque.append(cmd[1])

    elif cmd[0] == '3':
        if deque:
            print(deque.popleft())
        else:
            print(-1)

    elif cmd[0] =='4':
        if deque:
            print(deque.pop())
        else:
            print(-1)

    elif cmd[0] == '5':
        print(len(deque))

    elif cmd[0] == '6':
        if not deque:
            print(1)
        else:
            print(0)

    elif cmd[0] == '7':
        if deque:
            print(deque[0])
        else:
            print(-1)

    elif cmd[0] == '8':
        if deque:
            print(deque[-1])
        else:
            print(-1)