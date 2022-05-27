import math

def solution(progresses, speeds):
    date = []; rest_progresses = []; answer = []
    index = 0
        
    for i in progresses:
        rest_progresses.append(100-i)
    
    for i in range(len(progresses)):
        date.append(math.ceil(rest_progresses[i] / speeds[i]))
        
    for i in range(len(date)):
        if date[index] < date[i]:
            answer.append(i-index)
            index = i
    answer.append(len(date)-index)
    
    return answer