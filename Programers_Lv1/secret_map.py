def solution(n, arr1, arr2):
    answer = []
    map1_list = []
    map2_list = []
    str_sum_map = []
    
    for i in arr1:
        two = int(format(i, 'b'))
        map1_list.append(two)
    
    for i in arr2:
        two = int(format(i, 'b'))
        map2_list.append(two)
    
    for i in range(n):
        sum_map = str(map1_list[i]+map2_list[i])
        if len(sum_map) != n:
            sum_map = '0'*(n-len(sum_map)) + sum_map
        str_sum_map.append(sum_map)
    
    for i in str_sum_map:
        i = i.replace('0', ' ')
        i = i.replace('1', '#')
        i = i.replace('2', '#')
        answer.append(i)
        
    return answer

''' 다른 사람의 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):     # zip으로 하면 (i,j) 형태로 묶임
        a12 = str(bin(i|j)[2:])    # bin은 이진수로 바꿔주는 함수인데, 앞에 '0x'가 붙어서 [2:]로 슬라이싱 / 또한 | 는 or을 뜻하며 하나라도 1이 있으면 1로 반환
        a12=a12.rjust(n,'0')       # 오른쪽 정렬할때 사용 / 문자열.rjust(전체 자리 숫자, 공백이 있을 경우 공백을 채울 텍스트) 
                                     이외에도 문자열.zfill(문자열너비) -> "123".zfill(5) = "00123" 형태로 만들 수 있음
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''