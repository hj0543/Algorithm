while True:
    N = int(input())
    if N == 0:
        break
    
    rev_palin = str(N)[::-1]

    if str(N) == rev_palin:
        print('yes')
    else:
        print('no')