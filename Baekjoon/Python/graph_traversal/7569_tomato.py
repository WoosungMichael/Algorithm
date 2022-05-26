from collections import deque

M, N, H = map(int, input().split())

arr = []
cnt = 0
q = deque()
for i in range(H):
    tmp = []
    for j in range(N):
        tomato = list(map(int, input().split()))
        for k in range(len(tomato)):
            if tomato[k] == 0:
                cnt += 1
            elif tomato[k] == 1:
                q.append([i, j, k])
        tmp.append(tomato)
    arr.append(tmp)
q.append([-1, -1, -1])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

day = 0
if cnt == 0:
    print(0)

else:
    flag = True
    while cnt > 0:
        day += 1
        flag = True
        while q:
            i, j, k = q.popleft()
            if i == -1 and j == -1 and k == -1:
                q.append([-1, -1, -1])
                break
            for sur in range(6):
                if 0 <= i + dz[sur] < H and 0 <= j + dx[sur] < N and 0 <= k + dy[sur] < M and arr[i + dz[sur]][j + dx[sur]][k + dy[sur]] == 0:
                    arr[i + dz[sur]][j + dx[sur]][k + dy[sur]] = 1
                    q.append([i + dz[sur], j + dx[sur], k + dy[sur]])
                    cnt -= 1
                    flag = False
        if flag:
            break
        
    if flag:
        print(-1)
    else:
        print(day)