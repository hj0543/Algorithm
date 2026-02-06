word = input()

def palindrome_word (w):
    if w == w[::-1]:
        return '입력하신 단어는 회문(Palindrome)입니다.'
    
print(word)
print(palindrome_word(word))