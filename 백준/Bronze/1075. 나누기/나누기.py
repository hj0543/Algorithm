N = int(input())
F = int(input())

first = N // 100 * 100

i = 0
while True:
    if (first + i) % F == 0:
        number = str(first + i)
        break
    i += 1
 

print(number[-2:])