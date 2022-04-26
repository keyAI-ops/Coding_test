
def solution(absolutes, signs):
    signs = list(map(int, signs))
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == 0:
            signs[i] = -1
        answer += absolutes[i] * signs[i]
    return answer


'''
다른 사람의 풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
----------------------------------------------------------------------------------------------------
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer
'''
