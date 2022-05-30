from datetime import datetime

def solution(m, musicinfos):
    info = []
    info_time = []
    info_code = []
    answer = "(None)"
    
    for musicinfo in musicinfos:
        info.append(musicinfo.split(','))        
        
    for i in range(len(info)):
        # 시간차 구하기
        a = int(info[i][1][3:5])-int(info[i][0][3:5])  
        info_time.append(a)
        
        # 시간 동안 재생된 멜로디 구하기
        num = len(info[i][3]) - info[i][3].count('#')
        info_code.append(info[i][3]*(info_time[i]//num)+info[i][3][:info_time[i]%num])  
        
        if info_code[i].index(m) and 
    
    answer = info[i][2]

    return answer
