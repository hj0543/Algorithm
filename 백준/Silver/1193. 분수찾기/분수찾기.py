import sys
input = sys.stdin.readline

X = int(input()) # 14


# 현재의 위치 찾기
add = 0 # 15
for i in range(1, X + 1):
    add += i
    if add >= X:
        break

# 지금의 범위안의 수
my_range = i # 5


son_list = [] # [5, 4, 3, 2, 1]
mom_list = [] # [1, 2, 3, 4, 5]

for j in range(1, my_range + 1): # (1, 6) -> 1 ~ 5
    if my_range % 2 != 0: # 범위 안의 수가 홀수라면? -> 분모는 정순, 분자는 역순
        mom_list.append(j) 
        son_list.append(my_range + 1 - j)
    else:                 # 범위 안의 수가 짝수라면? -> 분모는 역순, 분자는 정순
        mom_list.append(my_range + 1 - j)
        son_list.append(j)

# 범위 안에서 나의 위치
my_location = X - (add - my_range) # 4

# 위치에서의 분자, 분모 값 호출
result_son = son_list[my_location - 1] # 2
result_mom = mom_list[my_location - 1] # 4
print(f'{result_son}/{result_mom}')