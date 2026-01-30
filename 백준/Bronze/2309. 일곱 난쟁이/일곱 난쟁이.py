import sys
input = sys.stdin.readline

height = []

for _ in range(9):
    n = int(input())
    height.append(n)

# 하나의 값 가져가면 제외하는 것 필요함



for i in range(9):
    for j in range(9):
        if i != j: # 두 값이 같지 않다면 (중복제거)
            if sum(height) - height[i] - height[j] == 100: # 만약에 두 값을 뺏을 때 100이 되는 두 값이 있다면
                del1 = height[i] # 제거할 변수 지정 1
                del2 = height[j] # 제거할 변수 지정 2

height.remove(del1) # height 리스트에서 변수1을 제거
height.remove(del2) # height 리스트에서 변수2을 제거

result = sorted(height) # 오름차순 출력해야하니 sorted로 따로 저장

for k in range(7): # 2명을 뺀 7명만 출력을 해야하니 범위는 7
    print(result[k])