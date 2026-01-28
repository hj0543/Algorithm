A = input()
B = input()
C = input()


my_dict = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,	
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}
result = int(str(my_dict.get(A)) + str(my_dict.get(B))) * (10 ** my_dict.get(C))
print(result)