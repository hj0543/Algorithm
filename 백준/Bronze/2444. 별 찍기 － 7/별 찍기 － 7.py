N = int(input())

i = 1
while i <= N:
    spaces = N - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)
    i += 1

j = N - 1
while j >= 1:
    spaces = N - j
    stars = 2 * j - 1
    print(' ' * spaces + '*' * stars)
    j -= 1