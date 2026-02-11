def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def comb(n, r):
    result = factorial(n) / (factorial(n - r) * factorial(r))
    return result


print(factorial(5))