# 자연수를 문자열로 입력한다.
h = input()
 
# 범위 확인을 위해 입력값을 정수로 변환
num_int = int(h)
 
num_list = [int(i) for i in h]

result = sum(num_list)
print(result)
