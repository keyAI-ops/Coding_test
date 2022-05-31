# K번째 수

def solution(array, commands):
    answer = []
    for com in commands:
        a = array[com[0]-1:com[1]]
        a.sort()
        answer.append(a[com[2]-1])    
    return answer

# 다른 사람의 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))