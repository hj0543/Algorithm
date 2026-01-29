import sys
input = sys.stdin.readline

S = int(input())



for i in range(S):
    num = list(map(int, input().split()))
    
    r = num[0]
    e = num[1]
    c = num[2]

    if r > e - c: # 광고 안 한 수익이 더 많으면 
        print('do not advertise')
    elif r < e - c: # 광고 한 수익이 더 많으면 
        print('advertise')
    else: # 같으면
        print('does not matter')