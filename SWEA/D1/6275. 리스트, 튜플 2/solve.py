sentence = list('Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.')

words = ['a', 'e', 'i', 'o', 'u']
for i in words:    
    while sentence.count(i) != 0:
        sentence.remove(i)

print(''.join(sentence))
