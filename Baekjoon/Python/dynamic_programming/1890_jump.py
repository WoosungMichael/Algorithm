N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

board = [[0] * N for i in range(N)]

board[0][0] = 1
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            if i + arr[i][j] < N:
                board[i + arr[i][j]][j] += board[i][j]
            if j + arr[i][j] < N:
                board[i][j + arr[i][j]] += board[i][j]

print(board[N - 1][N - 1] // 4)