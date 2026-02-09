import sys
input = sys.stdin.readline

S = list(map(str,input().strip()))
T = list(map(str,input().strip()))

while len(T) > len(S):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()

if S == T:
    print(1)
else:
    print(0)