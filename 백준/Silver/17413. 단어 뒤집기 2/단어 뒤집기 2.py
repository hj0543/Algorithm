S = input()


result = ""
temp = ""
inTag = False # 초기 inTag를 False 선언


for letter in S: 
    if letter == '<': # 글자가 '<' 라면
        result += temp[::-1] # 지금까지 쌓아둔 temp를 역으로 result에 삽입
        inTag = True # inTag True 선언
        result += letter # result 에 '<' 삽입
        temp = "" # temp 비우기


    elif letter == '>': # 글자가 '<' 라면
        inTag = False # inTag False 선언
        result += letter # result에 '>' 바로 삽입



    elif inTag: # inTag True 선언되어 있는 동안은
        result += letter # result에 바로 삽입    
        

    elif letter == ' ': # 공백을 만나면
        result += temp[::-1] + ' ' # 지금까지 쌓아둔 temp를 역으로 result에 삽입
        temp = "" # temp 비우기        


    else: # 태그 범위 밖의 일반 문자면
        temp += letter # temp에 글자를 쌓는다.


print(result + temp[::-1]) # 일반문자에서 끝날 경우를 생각해 지금까지 쌓아둔 temp를 result에 역으로 삽입해서 출력