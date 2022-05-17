def solution(n):
    answer = 0
    result_list = []
    list_num = [4,1,2]
    share = n//3
    rest = n%3
    
    while share // 3 == 0:
        result_list.append(rest)
        n = share // 3
    
    for i in 
        
        
        if rest == 0:
            result = str((share-1)*10+list_num[0])
        else:
            result = str(share*10+list_num[rest])
        return result