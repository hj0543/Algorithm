while True: # 무한 반복문을 시작함.
    try:
        A, B = map(int, input().split())
 
        print(A + B) # 0 0이 아닌 경우에만 → 두 수의 합을 출력함.
    except:
        break