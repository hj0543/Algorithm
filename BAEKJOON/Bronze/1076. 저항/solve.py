import sys
sys.stdin = open('input.txt', 'r')

A = input()
B = input()
C = input()

# 색에 따른 숫자 딕셔너리 생성
my_dict = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,	
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}
# A, B, 값을 문자로 받아와서 더한 다음 int로 변환 -> 10의 C제곱을 해서 앞의 값에 곱하면 저항값  나옴.
result = int(str(my_dict.get(A)) + str(my_dict.get(B))) * (10 ** my_dict.get(C))
print(result)
    
    