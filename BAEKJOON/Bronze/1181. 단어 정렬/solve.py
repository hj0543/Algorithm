import sys
sys.stdin = open('input.txt', 'r')


N = int(input())

nums_list = []

word_dict = {

}

reverse_dict = {

}


for _ in range(N):
    word = input()
    
    for i in range(N):
        word_dict.update({word:len(word)})
        reverse_dict.update({len(word):word})

    nums = word_dict.get(word)
    

    nums_list.append(nums)

val = sorted(nums_list)

for j in range(N):
    result = reverse_dict.get(val[j])

    print(result)    