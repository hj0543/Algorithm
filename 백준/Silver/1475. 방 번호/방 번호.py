N = input()

count = [0] * 10 # 0부터 10까지 초기설정

for i in N:
    number = int(i)
    count[number] += 1 # 각 숫자 나올때마다 count 에 해당 값 1씩 증가

cnt69 = (count[6] + count[9] + 1) // 2 # 합이 홀수인 경우를 고려해서 +1, 몫나눗셈

maxnum = 0 # 최빈값 0 초기설정
for j in range(10):
    if j != 6 and j != 9: # 6과 9가 아닐 때만 최빈값 계산
        if count[j] > maxnum: # 현재 최빈값 보다 높으면
            maxnum = count[j] # 높은 놈이 최빈값

if maxnum >= cnt69: # 최빈값이 69보다 같거나 크면
    print(maxnum) # 최빈값이 답이고
else:               # 아니면
    print(cnt69)    # 69가 답임