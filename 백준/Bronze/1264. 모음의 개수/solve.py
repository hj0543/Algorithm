import sys
sys.stdin = open('input.txt', 'r')


import sys

data = sys.stdin.read()

sentence = data.splitlines()

moeum = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


for i in range(len(sentence) - 1):
    total = 0
    for j in range(len(moeum)):
       cnt = (sentence[i]).count(moeum[j])
       total += cnt
    print(total)   


    # for i in range(len(mo)):
    #     result = S.find(mo[i])
    # print(result)