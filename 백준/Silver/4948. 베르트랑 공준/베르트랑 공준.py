import sys
input = sys.stdin.readline

def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

limit = 123456 * 2
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

while True:
    n = int(input())

    if n == 0:
        break

    print(sum(is_prime[n+1 : 2*n + 1]))