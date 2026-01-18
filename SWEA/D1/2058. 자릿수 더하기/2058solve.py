# 자연수를 문자열로 입력한다.
h = input()
 
# 범위 확인을 위해 입력값을 정수로 변환
num_int = int(h)
 
# 자연수가 1이상 9999이하인지 확인한다.
if 1 <= num_int <= 9999:
    # 조건을 만족하면 리스트 자료형을 사용하여 h 각 자리수를 표시한다.
    num_list = [int(i) for i in h]
    # h 각 자리수의 합을 구한다.
    result = sum(num_list)
    print(result)
else:
    print("범위 밖의 수입니다.")
