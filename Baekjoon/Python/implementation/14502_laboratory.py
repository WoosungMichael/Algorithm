from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

area0 = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            area0.append([i, j])

areaList = list(combinations(area0, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_cnt = 0
for i in areaList:
    tmp = copy.deepcopy(arr)
    for j in range(3):
        tmp[i[j][0]][i[j][1]] = 1
    visited = [[0] * M for _ in range(N)]

    area2 = deque()
    for x in range(N):
        for y in range(M):
            if tmp[x][y] == 2 and visited[x][y] == 0:
                area2.append([x, y])
                visited[x][y] = 1
                while area2:
                    tmp_x, tmp_y = area2.popleft()
                    tmp[tmp_x][tmp_y] = 2
                    for j in range(4):
                        if 0 <= tmp_x + dx[j] < N and 0 <= tmp_y + dy[j] < M and tmp[tmp_x + dx[j]][tmp_y + dy[j]] == 0 and visited[tmp_x + dx[j]][tmp_y + dy[j]] == 0:
                            area2.append([tmp_x + dx[j], tmp_y + dy[j]])
                            visited[tmp_x + dx[j]][tmp_y + dy[j]] = 1
    cnt = 0
    for x in range(N):
        for y in range(M):
            if tmp[x][y] == 0:
                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)