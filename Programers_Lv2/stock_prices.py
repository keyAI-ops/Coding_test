def solution(prices):
    answer = []
    while prices:
        result = 0
        a = prices.pop(0)
        for i in prices:
            if a <= i:
                result += 1
            else:
                result += 1
                break
        answer.append(result)
    return answer

''' 다른 사람의 풀이
from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer
'''