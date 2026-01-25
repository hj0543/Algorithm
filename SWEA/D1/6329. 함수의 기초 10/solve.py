def countdown (x):
    result = []
    if x == 0:
        return '카운트다운을 하려면 0보다 큰 입력이 필요합니다.'
    else:       
        for i in range(1, x + 1):           
            result.append(str(i))
            reversed_result = result[::-1]
            results = '\n'.join(reversed_result)
    return results
    
for j in (0, 10):
    print(countdown(j))
