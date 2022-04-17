# <문제> 바둑판에 흰 돌 놓기


n = int(input())

go_list = []
for _ in range(n):
    a = tuple(map(int, input().split()))
    go_list.append(a)

rows = 20
cols = 20
arr = [[0 for j in range(cols)] for i in range(rows)]

for i in go_list:
    arr[i[0]][i[1]] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(arr[i][j], end=' ')
    print()
