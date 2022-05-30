from collections import Counter

def solution(s):
    num_list = []
    answer = []

    s = s.split(",")
    for i in s:
        i = i.strip('{')
        i = i.strip('}')
        num_list.append(int(i))

    count_items = Counter(num_list).most_common()
    
    for i in count_items:
        answer.append(i[0])
    
    return answer
