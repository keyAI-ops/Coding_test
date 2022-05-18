def solution(N, stages):
    People = len(stages)
    fail_list = {}
    for i in range(1, N + 1):
        if People != 0:
            fail_list[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            fail_list[i] = 0

    return sorted(fail_list, key=lambda i: fail_list[i], reverse=True)