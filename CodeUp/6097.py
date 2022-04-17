# <문제> 설탕과자 뽑기

w, h = map(int, input().split())
k = int(input())

stick_list = []

for _ in range(k):
    stick_list.append(tuple(map(int, input().split())))

arr = [[0 for j in range(h+1)] for i in range(w+1)]

for i in range(k):
    if stick_list[i][1] == 0:
        for j in range(stick_list[i][0]):
            arr[stick_list[i][2]][stick_list[i][3]+j] = 1
    elif stick_list[i][1] == 1:
        for j in range(stick_list[i][0]):
            arr[stick_list[i][2]+j][stick_list[i][3]] = 1

for i in range(1, w+1):
    for j in range(1, h+1):
        print(arr[i][j], end=' ')
    print()
