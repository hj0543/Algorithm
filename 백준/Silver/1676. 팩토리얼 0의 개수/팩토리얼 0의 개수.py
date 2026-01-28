N = int(input())

def factorial(a): # 팩토리얼 함수
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact

fact_list = list(str(factorial(N))) # 팩토리얼 계산된 수를 리스트화 하고

rev_factlist = fact_list[::-1] # 역순으로 뒤집는다. (앞에서부터 계산하려고)

total = 0

for i in range(len(rev_factlist)):
    if rev_factlist[i] == '0': # rev_factlist 안에 있는 0은 문자열이다.
        total += 1
    else:
        break # 0이 아닌 숫자 나오면 즉시 탈출

print(total)