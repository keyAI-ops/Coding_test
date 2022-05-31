def solution(nums):
    answer = []
    pick_num = int(len(nums)/2)
    
    for i in nums:
        if i in answer:
            continue
        else:
            answer.append(i)
        if len(answer) == pick_num:
            break

    return len(answer)

# 다른 사람의 풀이
def solution(nums):
    return min(len(nums)/2, len(set(nums)))