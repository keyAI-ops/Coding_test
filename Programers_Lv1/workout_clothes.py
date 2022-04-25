
def solution(n, lost, reserve):
    answer = n-len(lost)

    lost.sort()
    reserve.sort()

    lost_1 = lost.copy()
    reserve_1 = reserve.copy()

    for lost_num in lost_1:
        if lost_num in reserve_1:
            answer += 1
            lost.remove(lost_num)
            reserve.remove(lost_num)

    for lost_num in lost:
        for reserve_num in reserve:
            if lost_num == reserve_num-1:
                reserve.remove(reserve_num)
                answer += 1
            elif lost_num == reserve_num+1:
                reserve.remove(reserve_num)
                answer += 1
    return answer


'''
다른 사람의 풀이

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''
