from collections import deque
N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1
L = int(input())
command = deque()
for i in range(L):
    X, C = input().split()
    command.append([X, C])

baam = deque()
baam.append([0, 0])
direction = 1 #0부터 상우하좌

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
flag = False
time = 0
tmp = 0
while True:
    if command:
        cmd = command.popleft()
    else:
        cmd = [tmp + N + 1, L]
    for i in range(int(cmd[0]) - tmp):
        time += 1
        if not(0 <= baam[0][0] + dx[direction] < N) or not(0 <= baam[0][1] + dy[direction] < N):
            flag = True
            break
        if [baam[0][0] + dx[direction], baam[0][1] + dy[direction]] in baam:
            flag = True
            break
        baam.appendleft([baam[0][0] + dx[direction], baam[0][1] + dy[direction]])
        if arr[baam[0][0]][baam[0][1]] == 0:
            baam.pop()
        else:
            arr[baam[0][0]][baam[0][1]] = 0
    if cmd[1] == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4
    if flag:
        break
    tmp = int(cmd[0])

print(time)