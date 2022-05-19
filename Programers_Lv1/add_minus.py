import math

def solution(left, right):
    sqrt1 = math.sqrt(left)
    sqrt2 = math.sqrt(right)
    answer = 0
    for i in range(left,right+1):
        if math.sqrt(i) % 1 == 0:
            answer -= i
        else:
            answer += i
    return answer