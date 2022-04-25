board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]
bucket = []
count = 0


def solution(board, moves):
    bucket = []
    count = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            bucket = bucket[:-2]
            count += 2
    print(count)
    return count


solution(board, moves)
