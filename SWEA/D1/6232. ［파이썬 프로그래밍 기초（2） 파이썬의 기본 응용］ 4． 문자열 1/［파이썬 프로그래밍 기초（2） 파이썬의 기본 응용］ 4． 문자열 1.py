word = str(input())

print(word)

list_word = list(word)

reverse_word = list(reversed(list_word))

if list_word == reverse_word:
    print('입력하신 단어는 회문(Palindrome)입니다.')