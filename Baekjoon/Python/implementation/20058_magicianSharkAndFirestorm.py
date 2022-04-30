from collections import deque

N, Q = map(int, input().split())

arr = []
for i in range(2 ** N):
    arr.append(list(map(int, input().split())))

L = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for q in range(Q):
    new_arr = [[] for _ in range(2 ** N)]
    for i in range((2 ** N) // (2 ** L[q])):
        for j in range((2 ** N) // (2 ** L[q])):
            for y in range((2 ** L[q]) * j, (2 ** L[q]) * (j + 1)):
                tmp = []
                for x in range((2 ** L[q]) * i, (2 ** L[q]) * (i + 1)):
                    tmp.append(arr[x][y])
                tmp = tmp[::-1]
                new_arr[y - (2 ** L[q]) * j + (2 ** L[q]) * i] += tmp

    erase = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            for d in range(4):
                if 0 <= i + dx[d] < 2 ** N and 0 <= j + dy[d] < 2 ** N and new_arr[i + dx[d]][j + dy[d]] > 0:
                    cnt += 1
            if cnt < 3 and new_arr[i][j] > 0:
                erase.append([i, j])

    for i in erase:
        new_arr[i[0]][i[1]] -= 1

    arr = new_arr

visited = [[0] * (2 ** N) for _ in range(2 ** N)]
total = 0
g_max = 0
for i in range(2 ** N):
    for j in range(2 ** N):
        total += arr[i][j]
        if arr[i][j] > 0 and visited[i][j] == 0:
            cnt = 0
            q = deque()
            q.append([i, j])
            visited[i][j] = 1
            while q:
                cnt += 1
                tmp = q.popleft()
                for d in range(4):
                    if 0 <= tmp[0] + dx[d] < 2 ** N and 0 <= tmp[1] + dy[d] < 2 ** N and arr[tmp[0] + dx[d]][tmp[1] + dy[d]] > 0 and visited[tmp[0] + dx[d]][tmp[1] + dy[d]] == 0:
                        q.append([tmp[0] + dx[d], tmp[1] + dy[d]])
                        visited[tmp[0] + dx[d]][tmp[1] + dy[d]] = 1
        if cnt > g_max:
            g_max = cnt

print(total)
print(g_max)