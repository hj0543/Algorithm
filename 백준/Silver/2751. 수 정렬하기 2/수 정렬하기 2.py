import sys
N = int(sys.stdin.readline())


numbers = [] # sort쓸거니까 빈 리스트에 저장하고


for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()  # sorted() 대신 in-place 정렬도 OK

output = '\n'.join(map(str, numbers))
sys.stdout.write(output)