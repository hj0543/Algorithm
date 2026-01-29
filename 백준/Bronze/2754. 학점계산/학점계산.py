import sys
input = sys.stdin.readline
C = list(input().strip())


grade1 = {
    'A': 4.0, 
    'B': 3.0, 
    'C': 2.0, 
    'D': 1.0, 
    'F': 0.0
}

grade2 = {
    '+': 0.3, 
    '0': 0.0, 
    '-': -0.3
}


if len(C) == 2:
    score = float(grade1.get(C[0]) + grade2.get(C[1]))
else:
    score = float(grade1.get(C[0]))
print(score)