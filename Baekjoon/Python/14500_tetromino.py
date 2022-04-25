N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

max_cnt = 0
for i in range(N):
    for j in range(M):
        if i + 3 < N:
            tmp = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
            if max_cnt < tmp:
                max_cnt = tmp
        if j + 3 < M:
            tmp = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
            if max_cnt < tmp:
                max_cnt = tmp

        if i + 2 < N and j > 0:
            tmp = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + max(arr[i][j - 1], arr[i + 1][j - 1], arr[i + 2][j - 1])
            if max_cnt < tmp:
                max_cnt = tmp
        if i + 2 < N and j + 1 < M:
            tmp = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + max(arr[i][j + 1], arr[i + 1][j + 1], arr[i + 2][j + 1])
            if max_cnt < tmp:
                max_cnt = tmp
        if i > 0 and j + 2 < M:
            tmp = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + max(arr[i - 1][j], arr[i - 1][j + 1], arr[i - 1][j + 2])        
            if max_cnt < tmp:
                max_cnt = tmp
        if i + 1 < N and j + 2 < M:
            tmp = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + max(arr[i + 1][j], arr[i + 1][j + 1], arr[i + 1][j + 2])
            if max_cnt < tmp:
                max_cnt = tmp
        
        if i + 1 < N and j + 1 < M:
            tmp = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
            if max_cnt < tmp:
                max_cnt = tmp

        if i + 2 < N and j + 1 < M:
            tmp = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            if max_cnt < tmp:
                max_cnt = tmp
        if i + 2 < N and j > 0:
            tmp = arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1] + arr[i + 2][j - 1]
            if max_cnt < tmp:
                max_cnt = tmp
        if i > 0 and j + 2 < M:
            tmp = arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i - 1][j + 2]
            if max_cnt < tmp:
                max_cnt = tmp
        if i + 1 < N and j + 2 < M:
            tmp = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
            if max_cnt < tmp:
                max_cnt = tmp

print(max_cnt)