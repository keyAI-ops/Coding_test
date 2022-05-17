from itertools import *

def solution(nums):
    result = 0
    a_list = list(combinations(nums, 3))
    sum_list = [sum(i) for i in a_list if sum(i)%2 != 0]
    
    for i in sum_list:
        fail_list = []
        for j in range(3,i,2):
            if i%j == 0:
                fail_list.append(j)
        if len(fail_list) == 0:
            result += 1
    return result

''' 다른 사람의 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

'''