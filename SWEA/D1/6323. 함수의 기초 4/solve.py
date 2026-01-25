import sys
sys.stdin = open('input.txt', 'r')

num = int(input())

# def fib(a):
#     nums = []
#     for i in range(1, a + 1):
#         for j in range(0, a, i):
#             fib_num = i + j
#             nums.append(fib_num)
#     return nums
# print(fib(num))

def fibonacci(n):
    nums = []
    a, b = 1, 1
    for i in range(0, n):
        nums.append(a)
        a, b = b, a + b # 이 부분이 중요한거임!
    return nums

print(fibonacci(num))

