import sys

while True:

    a, b = map(int, sys.stdin.readline().split())
    
    if a == 0 and b == 0: # 둘 다 0이면 루프 탈출
        break

    print(a + b)