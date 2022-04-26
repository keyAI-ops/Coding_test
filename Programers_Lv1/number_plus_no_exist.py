def solution(numbers):
    full_sum = 0
    for i in range(1, 10):
        full_sum += i
    answer = full_sum - sum(numbers)
    return answer
