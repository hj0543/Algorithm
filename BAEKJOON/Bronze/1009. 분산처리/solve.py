import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    result = pow(a, b, 10)
    print(10 if result == 0 else result)

'''
>> pow

pow(a, b) == a ** b
pow(a, b, c) == (a ** b) % c

>> 삼항연산자

print(값1 if 조건 else 값2)
조건 : 참 => 값1
조건 : 거짓 => 값2
'''