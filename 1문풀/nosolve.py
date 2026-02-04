# import sys
# sys.stdin = open('input.txt', 'r')
#
# # 1193
# import sys
# input = sys.stdin.readline
arr = [19, 6, 16, 19, 15, 16, 8, 13, 16, 10]

def subset(my_list):
    n = len(my_list) # n : 원소의 개수
    result = []
    for i in range(1<<n): # 1<<n : 부분 집합의 개수
        temp_subset = []
        for j in range(n): # 원소의 수만큼 비트를 비교함
            list1 = []
            if i & (1<<j):          # i의 j번 비트가 1인경우
                temp_subset.append(my_list[j])
                list1.append(result)
        result.append(temp_subset)
    return result



