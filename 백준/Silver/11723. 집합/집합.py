import sys
input = sys.stdin.readline

M = int(input())

set_ = set()

for i in range(M):
    cmd = input().split()

    if cmd[0]=='add':
        if int(cmd[1]) not in set_:
            set_.add(int(cmd[1]))

    elif cmd[0]=='remove':
        if int(cmd[1]) in set_:
            set_.discard(int(cmd[1]))

    elif cmd[0]=='check':
        if int(cmd[1]) in set_:
            print(1)
        else:
            print(0)

    elif cmd[0]=='toggle':
        if int(cmd[1]) in set_:
            set_.remove(int(cmd[1]))
        else:
            set_.add(int(cmd[1]))

    elif cmd[0]=='all':
        set_ = set(range(1, 21))
        continue

    elif cmd[0]=='empty':
        set_ = set()
        continue