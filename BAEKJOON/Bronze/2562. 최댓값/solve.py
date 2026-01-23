import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split())) # list

print(A)
# sorted_A = sorted(A)


# ans = []
# i = 0
# while i < N:

#     if A[i] < X: # A[i]를 통해 리스트 위치에 따라 순차적으로 검사
#         ans.append(str(A[i])) # A[i] < X를 만족하면 ans리스트에 만족하는 A 리스트 값 추가
#     i += 1 # 다음 리스트 순번 검사를 위해 추가