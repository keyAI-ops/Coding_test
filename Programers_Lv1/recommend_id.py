def solution(new_id):
    answer = ''
    answer += new_id.lower()

    for i in answer:
        if not ((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 45 or ord(i) == 46 or ord(i) == 95):
            answer = answer.replace(i, '')

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer.strip('.')

    if len(answer) == 0:
        answer += "a"

    if len(answer) >= 16:
        answer = answer[:15]

    answer = answer.strip('.')

    if len(answer) <= 2:
        for i in range(3-len(answer)):
            answer += answer[-1]

    return answer
