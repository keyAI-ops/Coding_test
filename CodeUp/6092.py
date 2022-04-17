# <문제> 이상한 출석 번호 부르기1

n = int(input())
a = list(map(int, input().split()))

num_list = [0]*24

for i in a:
    num_list[i] += 1

for i in range(1, 24):
    print(num_list[i], end=' ')
