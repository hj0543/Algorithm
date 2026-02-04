import sys
sys.stdin = open('input.txt', 'r')

# 2578
import sys
input = sys.stdin.readline

def my_len(arr):
    cnt = 0
    for _ in arr:
        cnt += 1
    return cnt

def my_sum(arr):
    total = 0
    for i in range(my_len(arr)):
        total += arr[i]
    return total

def my_max(arr):
    max_num = arr[0]
    for i in range(my_len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num

for _ in range(10):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]

    total = []
    for i in range(100):
        total.append(my_sum(grid[i]))

    for i in range(100):
        add1 = 0
        for j in range(100):
            add1 += grid[j][i]
        total.append(add1)


    add2 = 0
    for i in range(100):
        add2 += grid[i][i]
    total.append(add2)

    add3 = 0
    for i in range(100):
        add3 += grid[i][99-i]
    total.append(add3)

    print(f'#{_+1} {my_max(total)}')


