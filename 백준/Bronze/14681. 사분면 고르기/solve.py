x = int(input())  # A, B = map(int, input().split()) 이렇게 풀면 안됨. 문제에서 세로 배열로 줬기 때문
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
else:
    print(3)