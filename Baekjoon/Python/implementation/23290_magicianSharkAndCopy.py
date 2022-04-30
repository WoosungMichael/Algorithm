M, S = map(int, input().split())

arr = [[0] * 4 for _ in range(4)]
fish = []
smell = [[[0] * 4 for _ in range(4)] for __ in range(3)]

for i in range(M):
    tmp = list(map(int, input().split()))
    tmp[0] -= 1
    tmp[1] -= 1
    tmp[2] -= 1
    fish.append(tmp)
    arr[tmp[0]][tmp[1]] += 1

shark = list(map(int, input().split()))
shark[0] -= 1
shark[1] -= 1

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx1 = [-1, 0, 1, 0]
dy1 = [0, -1, 0, 1]

for i in range(S):
    new_fish = []
    for j in range(len(fish)):
        flag = True
        cnt = 0
        tmp = fish[j][2]
        while flag:
            if [fish[j][0] + dx[tmp], fish[j][1] + dy[tmp]] != [shark[0], shark[1]] and 0 <= fish[j][0] + dx[tmp] < 4 and 0 <= fish[j][1] + dy[tmp] < 4 and smell[(i + 1) % 3][fish[j][0] + dx[tmp]][fish[j][1] + dy[tmp]] == 0 and smell[(i + 2) % 3][fish[j][0] + dx[tmp]][fish[j][1] + dy[tmp]] == 0:
                new_fish.append([fish[j][0] + dx[tmp], fish[j][1] + dy[tmp], tmp])
                arr[fish[j][0]][fish[j][1]] -= 1
                arr[fish[j][0] + dx[tmp]][fish[j][1] + dy[tmp]] += 1
                flag = False
            else:
                tmp = (tmp + 7) % 8
                cnt += 1
                if cnt == 8:
                    new_fish.append([fish[j][0], fish[j][1], tmp])
                    break

    g_coor = []
    global_max = -1
    s_x, s_y = 0, 0
    g_tmp_new = []
    for a in range(4):
        for b in range(4):
            for c in range(4):
                coor = []
                tmp_cnt = 0
                tmp_smell = []
                tmp_new = []
                x, y = shark[0], shark[1]
                flag_fin = True

                if 0 <= x + dx1[a] < 4 and 0 <= y + dy1[a] < 4:
                    x += dx1[a]
                    y += dy1[a]
                    if arr[x][y] > 0:
                        for nf in new_fish:
                            if nf[0] == x and nf[1] == y:
                                tmp_new.append(nf)
                        tmp_cnt += arr[x][y]
                        coor.append([x, y, arr[x][y]])
                        arr[x][y] = 0
                        tmp_smell.append([x, y])
                else:
                    flag_fin = False

                if flag_fin and 0 <= x + dx1[b] < 4 and 0 <= y + dy1[b] < 4:
                    x += dx1[b]
                    y += dy1[b]
                    if arr[x][y] > 0:
                        for nf in new_fish:
                            if nf[0] == x and nf[1] == y:
                                tmp_new.append(nf)
                        tmp_cnt += arr[x][y]
                        coor.append([x, y, arr[x][y]])
                        arr[x][y] = 0
                        tmp_smell.append([x, y])
                else:
                    flag_fin = False

                if flag_fin and 0 <= x + dx1[c] < 4 and 0 <= y + dy1[c] < 4:
                    x += dx1[c]
                    y += dy1[c]
                    if arr[x][y] > 0:
                        for nf in new_fish:
                            if nf[0] == x and nf[1] == y:
                                tmp_new.append(nf)
                        tmp_cnt += arr[x][y]
                        coor.append([x, y, arr[x][y]])
                        arr[x][y] = 0
                        tmp_smell.append([x, y])
                else:
                    flag_fin = False


                if tmp_cnt > global_max and flag_fin:
                    global_max = tmp_cnt
                    smell[i % 3] = [[0] * 4 for _ in range(4)]
                    for ts in tmp_smell:
                        smell[i % 3][ts[0]][ts[1]] = 1
                    for co in coor:
                        arr[co[0]][co[1]] += co[2]
                    g_coor = coor
                    g_tmp_new = [[0] * 4 for _ in range(4)]
                    for tn in tmp_new:
                        g_tmp_new[tn[0]][tn[1]] = 1
                    s_x, s_y = x, y
                else:
                    for co in coor:
                        arr[co[0]][co[1]] += co[2]

    tmp_tmp = []
    for nf in new_fish:
        if g_tmp_new[nf[0]][nf[1]] == 0:
            tmp_tmp.append(nf)

    for g_c in g_coor:
        arr[g_c[0]][g_c[1]] = 0

    shark = [s_x, s_y]
    for c in g_coor:
        arr[c[0]][c[1]] = 0

    for f in fish:
        arr[f[0]][f[1]] += 1
    fish += tmp_tmp

answer = 0
for i in range(4):
    for j in range(4):
        answer += arr[i][j]
print(answer)
