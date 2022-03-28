N, K = map(int, input().split())
arr = list(map(int, input().split()))

start_i = 0
robot = []
stage_cnt = 0
cnt_0 = 0
while True:
    stage_cnt += 1
    start_i -= 1
    if start_i < 0:
        start_i += 2 * N
    for i in robot[:]:
        if i == (start_i + N - 1) % (2 * N):
            robot.remove(i)
            continue
        if arr[(i + 1) % (2 * N)] != 0 and (i + 1) % (2 * N) not in robot:
            arr[(i + 1) % (2 * N)] -= 1
            if arr[(i + 1) % (2 * N)] == 0:
                cnt_0 += 1
            if (i + 1) % (2 * N) != (start_i + N - 1) % (2 * N):
                robot.append((i + 1) % (2 * N))
            robot.remove(i)
    if arr[start_i] != 0:
        robot.append(start_i)
        arr[start_i] -= 1
        if arr[start_i] == 0:
            cnt_0 += 1
    if cnt_0 >= K:
        break
    
print(stage_cnt)