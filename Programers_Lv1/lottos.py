def solution(lottos, win_nums):
    answer = []
    zero_count = lottos.count(0)
    count = 0

    for lotto in lottos:
        if lotto == 0:
            continue
        count += win_nums.count(lotto)

    high_low_count = [count+zero_count, count]
    answer = []

    for i in high_low_count:
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)
    return answer


''' 다른 사람 풀이
def solution(lottos, win_nums):
    
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''
