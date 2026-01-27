T = int(input())
text = [str(input()) for i in range(T)]

for i in text:
    print(i[0] + i[-1])