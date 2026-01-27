A = int(input())
B = int(input())
C = int(input())

multi = str(A * B * C)

print(multi.count('0'))
for i in range(1, 10):
    
    print(multi.count(str(i)))