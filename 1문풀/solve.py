import sys
sys.stdin = open('input.txt', 'r')

# 1193
import sys
input = sys.stdin.readline

################################################

def my_len(my_list):
    cnt = 0

    for i in my_list:
        cnt += 1
    return cnt

################################################

def my_max(my_list):
    max_num = my_list[0]
    for i in range(my_len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]
    return max_num

###############################################

def my_min(my_list):
    min_num = my_list[0]
    for i in range(my_len(my_list)):
        if my_list[i] < min_num:
            min_num = my_list[i]
    return min_num

################################################

for t in range(10):
    N = int(input())
    H = list(map(int, input().split()))

    num = 0

    
    while num <= N:
        max_height = my_max(H)
        min_height = my_min(H)

        max_index = H.index(max_height)
        H[max_index] -= 1

        min_index = H.index(min_height)
        H[min_index] += 1        

        num += 1
        
    print(f'#{t+1} {max_height - min_height}')







