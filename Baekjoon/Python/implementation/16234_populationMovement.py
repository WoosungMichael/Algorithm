from collections import deque

N, L, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [0, 1]
dy = [1, 0]

day = 0

dx1 = [-1, 1, 0, 0]
dy1 = [0, 0, -1, 1]

while True:
    flag = True
    wall = [[[1, 1] for _ in range(N)] for __ in range(N)] # wall[i][j][0] = 오른쪽 벽 wall[i][j][1] = 아래 벽
    for i in range(N):
        for j in range(N):
            for way in range(2):
                if 0 <= i + dx[way] < N and 0 <= j + dy[way] < N and L <= max(arr[i][j] - arr[i + dx[way]][j + dy[way]], arr[i + dx[way]][j + dy[way]] - arr[i][j]) <= R:
                    wall[i][j][way] = 0

    visited = [[0] * N for _ in range(N)]

    area = deque()
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                area.append([x, y])
                visited[x][y] = 1
                tmp = []
                cnt = 0
                area_sum = 0
                while area:
                    [i, j] = area.popleft()
                    tmp.append([i, j])
                    cnt += 1
                    area_sum += arr[i][j]
                    if 0 <= i - 1 and wall[i - 1][j][1] == 0 and visited[i - 1][j] == 0:
                        area.append([i - 1, j])
                        visited[i - 1][j] = 1
                    if i + 1 < N and wall[i][j][1] == 0 and visited[i + 1][j] == 0:
                        area.append([i + 1, j])
                        visited[i + 1][j] = 1
                    if 0 <= j - 1 and wall[i][j - 1][0] == 0 and visited[i][j - 1] == 0:
                        area.append([i, j - 1])
                        visited[i][j - 1] = 1
                    if j + 1 < N and wall[i][j][0] == 0 and visited[i][j + 1] == 0:
                        area.append([i, j + 1])
                        visited[i][j + 1] = 1
                zone = area_sum // cnt
                for z in tmp:
                    if arr[z[0]][z[1]] != zone:
                        arr[z[0]][z[1]] = zone
                        flag = False

    if flag:
        break
    day += 1

print(day)