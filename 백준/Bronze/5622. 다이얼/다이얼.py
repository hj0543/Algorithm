S = input()

dial_dict = {
    'ABC' : 2,
    'DEF' : 3,
    'GHI' : 4,
    'JKL' : 5,
    'MNO' : 6,
    'PQRS' : 7,
    'TUV' : 8,
    'WXYZ' : 9
}

total = 0

for i in S:
    for j in dial_dict: # i = dial_dict의 key
            if i in j:
                  total += dial_dict[j]

print(total + len(S))