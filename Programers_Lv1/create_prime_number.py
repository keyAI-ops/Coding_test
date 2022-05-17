from itertools import *

def solution(nums):
    result = 0
    a_list = list(combinations(nums, 3))
    sum_list = [sum(i) for i in a_list if sum(i)%2 != 0]
    
    for i in sum_list:
        f_list = []
        for j in range(3,i,2):
            if i%j == 0:
                f_list.append(j)
        if len(f_list) == 0:
            result += 1
    return result