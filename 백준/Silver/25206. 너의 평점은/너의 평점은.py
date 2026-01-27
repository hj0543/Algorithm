scores_dict = {
    'A+' : '4.5',
    'A0' : '4.0',
    'B+' : '3.5',
    'B0' : '3.0',
    'C+' : '2.5',
    'C0' : '2.0',
    'D+' : '1.5',
    'D0' : '1.0',
    'F' : '0.0'
}
total_score = 0
total_time = 0
for _ in range(20):
    scores = input().split()

    for i in range(20):        
        if scores[-1] != 'P':
            add = float(scores[1]) * float(scores_dict.get(scores[-1]))
            total_score += add
            total_time += float(scores[1])
                    
print(total_score / total_time)