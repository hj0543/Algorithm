A, B = map(str, input().split(', '))

def compare (x, y):
    if len(x) > len(y):
        return x
    else:
        return y
    
print(compare(A, B))
