A, B = map(int, input().split(','))

def square (x):
    result = x ** 2
    return result

for i in (A, B):
    print(f'square({i}) => {square(i)}')