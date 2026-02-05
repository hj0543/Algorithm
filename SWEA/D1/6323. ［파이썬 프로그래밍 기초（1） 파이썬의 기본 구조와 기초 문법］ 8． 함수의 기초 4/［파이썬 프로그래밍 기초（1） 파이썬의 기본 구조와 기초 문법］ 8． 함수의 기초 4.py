num = int(input())

def fibonacci(n):
    nums = []
    a, b = 1, 1
    for i in range(0, n):
        nums.append(a)
        a, b = b, a + b
    return nums

print(fibonacci(num))
