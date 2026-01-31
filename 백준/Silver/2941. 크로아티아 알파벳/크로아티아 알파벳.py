import sys
words = sys.stdin.readline().strip()


croatia = {
    'c=': '*',
    'c-': '*',
    'dz=': '*',
    'd-': '*',
    'lj': '*',
    'nj': '*', 
    's=': '*', 
    'z=': '*'
}

# words 내부에 있는 모든 key를 찾아 *로 바꾼다.
for k in croatia:
    words = words.replace(k, croatia[k]) # key, value

print(len(words))