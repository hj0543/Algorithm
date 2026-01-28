N = int(input())



for _ in range(N):
    line = input().split()
    
    init = float(line[0]) # 초기값 line 0번 설정


    for i in line[1:]: # 1부터 i가 @면 *3, %면 +5, #이면 -7
        if i == '@':
            init *= 3
        elif i == '%':
            init += 5
        elif i == '#':
            init -= 7

    print(f'{init:.2f}') # 소수 둘째자리까지