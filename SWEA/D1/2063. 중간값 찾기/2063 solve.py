h = input()
 
# 정수를 문자열로 변환한다.
num_int = int(h)
 
# N은 9이상 199이하인지, N이 홀수인지
if (9 <= num_int <= 199) and (num_int % 2 != 0):
     
    # 문자열을 리스트 자료형 오름차순으로 나타낸다.
    scores = list(map(int, input().split()))
    scores.sort()
    # 중앙값을 구하고 출력한다.
    med_scores = scores[num_int //2]
    print(med_scores)
else:
    print("입력된 N이 제약 조건에 맞지 않습니다.")
