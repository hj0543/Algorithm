def factorial(a): # 팩토리얼 함수
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact

 # 조합 = M!/ (M-m)! * m!

def comb(x, y): # 조합 함수 (x < y)
    result = factorial(y) // (factorial(y - x) * factorial(x))  # //으로 하면 되나...?  
    return result


n, m = map(int, input().split())

print(int(comb(m, n)))