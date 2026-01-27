import sys
sys.stdin = open('input.txt', 'r')

N = int(input())


group_number = N # 초기 그룹단어 개수 N으로 설정


for _ in range(N):
    word = input()

    for i in range(len(word) - 1): # 전체 길이의 1감소한만큼만 검사한다.
        if word[i] != word[i + 1]: # 이어진 글자가 같지 않다면
            if word[i] in word[i + 1:]: # 두 칸 이상 떨어진 수가 있다면
                group_number -= 1 # 그룹단어 개수에서 1 뺀다.
                break # 이미 그룹 단어가 아니므로, 더 검사하지 말고 탈출!
            
print(group_number)
        


    
    