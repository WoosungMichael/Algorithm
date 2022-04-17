def bfs(arr, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    max_cnt = 0
    erase = []
    #visited배열 한번만 쓰고 0만 초기화해주면서 arr[i][j]가 자연수 and visited[i][j] != 0일때만 돌게
    for i in range(N):
        for j in range(N):
            value = arr[i][j]
            queue = [(i, j)]
            visited = [[0] * N for i in range(N)]
            cnt = 0
            while queue:
                x, y = queue.pop()
                visited[x][y] = 1
                for k in range(4):
                    if 0 <= x + dx[k] and x + dx[k] < N and 0 <= y + dy[k] and y + dy[k] < N and visited[x + dx[k]][y + dy[k]] == 0:
                        if arr[x + dx[k]][y + dy[k]] == value or arr[x + dx[k]][y + dy[k]] == 0:
                            queue.append((x + dx[k], y + dy[k]))
                cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                erase = []
                for x in range(N):
                    for y in range(N):
                        if visited[x][y] == 1:
                            erase.append((x, y))
    if max_cnt >= 2:
        for (i, j) in erase:
            arr[i][j] = -2
        
        #for j in range(N):
            

    else:
        return 

    

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

bfs(arr, N)