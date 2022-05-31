# 다른 사람의 풀이

from itertools import permutations

def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')  # '구분자'.join(합칠 것) : 구분자를 넣어서 합친다.
        answer.append(abs(eval(a.join(temp_list))))  # eval : 문자열로 된 수식을 계산
    return max(answer)

# 다른 사람의 풀이 2

def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    for oper in permutations(operators, 3):
        a = oper[0]  # ('*', '+', '-') 중 0번째
        b = oper[1]
        tmp_list = []
        for i in expression.split(a): 
            tmp = [f"({j})" for j in i.split(b)]
            tmp_list.append(f"({b.join(tmp)})")
        answer.append(abs(eval(a.join(tmp_list))))
    return max(answer)