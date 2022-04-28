N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

before = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

dx1 = [-1, -1, 1, 1]
dy1 = [-1, 1, -1 , 1]

for i in range(M):
    d, s = map(int, input().split())
    b = [([0] * N) for _ in range(N)]
    for j in range(len(before)):
        before[j] = [(before[j][0] + dx[d] * s + N * 25) % N, (before[j][1] + dy[d] * s + N * 25) % N]
        b[before[j][0]][before[j][1]] = 1
    for xy in before:
        arr[xy[0]][xy[1]] += 1
    for xy in before:
        cnt = 0
        for index in range(4):
            if 0 <= xy[0] + dx1[index] < N and 0 <= xy[1] + dy1[index] < N and arr[xy[0] + dx1[index]][xy[1] + dy1[index]] > 0:
                cnt += 1
        arr[xy[0]][xy[1]] += cnt
    after = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] >= 2 and b[x][y] == 0:
                arr[x][y] -= 2
                after.append([x, y])
    before = after

g_sum = 0
for i in range(N):
    g_sum += sum(arr[i])
print(g_sum)