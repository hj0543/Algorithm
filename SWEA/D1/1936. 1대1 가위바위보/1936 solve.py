# A, B값을 입력받는다.
a, b = map(int, input().split())

# 차이를 계산한다.
result = a - b

# 차이가 -1 또는 2이면 B가 이긴다.
if result == -1 or result == 2:
	print("B")
else:
	print("A")
