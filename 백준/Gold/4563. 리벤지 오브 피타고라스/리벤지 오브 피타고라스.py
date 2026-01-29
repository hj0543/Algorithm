import sys

input_data = sys.stdin.read().split()

for i in input_data:
    a = int(i)
    
    # 0이 입력되면 반복문을 종료
    if a == 0:
        break
    
    a_sq = a * a
    count = 0
    

    for m in range(1, a): # 1 부터 a까지
        if a_sq % m == 0: # a제곱을 m으로 나눠떨어지면
            n = a_sq // m # n은 a제곱을 m으로 나눈 값이라 한다
            
            if (n + m) % 2 == 0: # m + n 이 짝수라면
                b = (n - m) // 2 # n - m 을 2로 나눈 값을 b라 하자
                if b > a: # b가 a 보다 크면 1 count한다.
                    count += 1
    
    print(count)