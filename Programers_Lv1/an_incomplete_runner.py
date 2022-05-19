def solution(participant, completion):
    participant.sort()
    completion.sort()
    for _ in range(len(completion)):
        participant.remove(completion.pop())
    answer = participant[0]
    return answer

''' 
다른 사람의 풀이 
def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("1")
    answer=""
    for i in range(0,len(completion)):
        if participant[i] != completion[i]:
            answer=participant[i]
            return answer
'''