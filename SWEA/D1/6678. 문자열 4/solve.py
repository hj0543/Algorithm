import sys
sys.stdin = open('input.txt', 'r')

while True:
    try:
        s = input()
        if s == "":
            break
        print(f'>> {s.upper()}')
    except EOFError:
        break