S = int(input())

total = 0
cnt = 0

for i in range(1, S + 1): # S가 1일때도 있으니 S + 1까지
    if total + i <= S: # i에 지금까지 더한 수를 더했을 때 S보다 작다면
        total += i # total에 i + 1을 더하고
        cnt += 1 # 지금까지 더한 자연수의 개수를 1개 더한다.
    else:   
        break # i가 자연수의 합에서 지금까지 더한 수를 뺀 것 보다 크다면 탈출
print(cnt)