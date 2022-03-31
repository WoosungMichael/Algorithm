def moveUp(arr, r_x, r_y, b_x, b_y, cnt):
    cnt += 1
    tmp_r = r_x
    flag_r = False
    for i in range(r_x - 1, 0, -1):
        if arr[i][r_y] == '.':
            tmp_r = i
        elif arr[i][r_y] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[i][r_y] == '0':
            arr[tmp_r][r_y] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp_r][r_y] = 'R'
    r_x = tmp_r

    tmp_b = b_x
    flag_b = False
    for i in range(b_x - 1, 0, -1):
        if arr[i][b_y] == '.':
            tmp_b = i
        elif arr[i][b_y] == '#' or arr[i][b_y] == 'R':
            break
        elif arr[i][b_y] == '0':
            arr[tmp_b][b_y] = '.'
            flag_b = True
            break
    arr[b_x][b_y] = '.'
    if not flag_b:
       arr[tmp_b][b_y] = 'B'
    b_x = tmp_b

    for i in range(r_x - 1, 0, -1):
        if arr[i][r_y] == '.':
            tmp_r = i
        elif arr[i][r_y] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[i][r_y] == '0':
            arr[tmp_r][r_y] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp_r][r_y] = 'R'
    r_x = tmp_r

    return arr, r_x, r_y, b_x, b_y, flag_r, flag_b, cnt

def moveDown(arr, r_x, r_y, b_x, b_y, cnt):
    cnt += 1
    tmp_r = r_x
    flag_r = False
    for i in range(r_x + 1, N):
        if arr[i][r_y] == '.':
            tmp_r = i
        elif arr[i][r_y] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[i][r_y] == '0':
            arr[tmp_r][r_y] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp_r][r_y] = 'R'
    r_x = tmp_r

    tmp_b = b_x
    flag_b = False
    for i in range(b_x + 1, N):
        if arr[i][b_y] == '.':
            tmp_b = i
        elif arr[i][b_y] == '#' or arr[i][b_y] == 'R':
            break
        elif arr[i][b_y] == '0':
            arr[tmp_b][b_y] = '.'
            flag_b = True
            break
    arr[b_x][b_y] = '.'
    if not flag_b:
        arr[tmp_b][b_y] = 'B'
    b_x = tmp_b

    for i in range(r_x + 1, N):
        if arr[i][r_y] == '.':
            tmp_r = i
        elif arr[i][r_y] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[i][r_y] == '0':
            arr[tmp_r][r_y] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp_r][r_y] = 'R'
    r_x = tmp_r

    return arr, r_x, r_y, b_x, b_y, flag_r, flag_b, cnt
    
def moveLeft(arr, r_x, r_y, b_x, b_y, cnt):
    cnt += 1
    tmp_r = r_y
    flag_r = False
    for i in range(r_y - 1, 0, -1):
        if arr[r_x][i] == '.':
            tmp_r = i
        elif arr[r_x][i] == '#' or arr[r_x][i] == 'B':
            break
        elif arr[r_x][i] == '0':
            arr[r_x][tmp_r] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[r_x][tmp_r] = 'R'
    r_y = tmp_r

    tmp_b = b_y
    flag_b = False
    for i in range(b_y - 1, 0, -1):
        if arr[b_x][i] == '.':
            tmp_b = i
        elif arr[b_x][i] == '#' or arr[b_x][i] == 'R':
            break
        elif arr[b_x][i] == '0':
            arr[b_x][tmp_b] = '.'
            flag_b = True
            break
    arr[b_x][b_y] = '.'
    if not flag_b:
        arr[b_x][tmp_b] = 'B'
    b_y = tmp_b

    for i in range(r_y - 1, 0, -1):
        if arr[r_x][i] == '.':
            tmp_r = i
        elif arr[r_x][i] == '#' or arr[r_x][i] == 'B':
            break
        elif arr[r_x][i] == '0':
            arr[r_x][tmp_r] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[r_x][tmp_r] = 'R'
    r_y = tmp_r

    return arr, r_x, r_y, b_x, b_y, flag_r, flag_b, cnt
    
def moveRight(arr, r_x, r_y, b_x, b_y, cnt):
    cnt += 1
    tmp_r = r_y
    flag_r = False
    for i in range(r_y + 1, M):
        if arr[r_x][i] == '.':
            tmp_r = i
        elif arr[r_x][i] == '#' or arr[r_x][i] == 'B':
            break
        elif arr[r_x][i] == '0':
            arr[r_x][tmp_r] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[r_x][tmp_r] = 'R'
    r_y = tmp_r

    tmp_b = b_y
    flag_b = False
    for i in range(b_x + 1, M):
        if arr[b_x][i] == '.':
            tmp_b = i
        elif arr[b_x][i] == '#' or arr[b_x][i] == 'R':
            break
        elif arr[b_x][i] == '0':
            arr[b_x][tmp_b] = '.'
            flag_r = True
            break
    arr[b_x][b_y] = '.'
    if not flag_b:
        arr[b_x][tmp_b] = 'B'
    b_y = tmp_b

    for i in range(r_y + 1, M):
        if arr[r_x][i] == '.':
            tmp_r = i
        elif arr[r_x][i] == '#' or arr[r_x][i] == 'B':
            break
        elif arr[r_x][i] == '0':
            arr[r_x][tmp_r] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[r_x][tmp_r] = 'R'
    r_y = tmp_r

    return arr, r_x, r_y, b_x, b_y, flag_r, flag_b, cnt
    

def checkRoute(arr, r_x, r_y, b_x, b_y, cnt):
    global min
    
    if arr[r_x - 1][r_y] != '#':
        tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt = arr, r_x, r_y, b_x, b_y, cnt
        tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, flag_r, flag_b, tmp_cnt = moveUp(tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt)
        if flag_r and not flag_b:
            if min > tmp_cnt:
                min = tmp_cnt
        elif tmp_cnt != 11:
            tmp_cnt = checkRoute(tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt)

    if arr[r_x + 1][r_y] != '#':
        tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt = arr, r_x, r_y, b_x, b_y, cnt
        tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, flag_r, flag_b, tmp_cnt = moveDown(tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt)
        if flag_r and not flag_b:
            if min > tmp_cnt:
                min = tmp_cnt
        elif tmp_cnt != 11:
            tmp_cnt = checkRoute(tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt)

    if arr[r_x][r_y - 1] != '#':
        tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt = arr, r_x, r_y, b_x, b_y, cnt
        tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, flag_r, flag_b, tmp_cnt = moveLeft(tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt)
        if flag_r and not flag_b:
            if min > tmp_cnt:
                min = tmp_cnt
        elif tmp_cnt != 11:
            tmp_cnt = checkRoute(tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt)

    if arr[r_x][r_y + 1] != '#':
        tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt = arr, r_x, r_y, b_x, b_y, cnt
        tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, flag_r, flag_b, tmp_cnt = moveRight(tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt)
        if flag_r and not flag_b:
            if min > tmp_cnt:
                min = tmp_cnt
        elif tmp_cnt != 11:
            tmp_cnt = checkRoute(tmp_arr, tmp_rx, tmp_ry, tmp_bx, tmp_by, tmp_cnt)

    return min
    
    

N, M = map(int, input().split())

arr = []

r_x, r_y = 0, 0
b_x, b_y = 0, 0
x, y = 0, 0
for i in range(N):
    tmp = list(input())
    arr.append(tmp)
    for j in range(len(tmp)):
        if arr[i][j] == 'R':
            r_x, r_y = i, j
        if arr[i][j] == 'B':
            b_x, b_y = i, j
        if arr[i][j] == '0':
            x, y = i, j

cnt = 0
global min
min = 11
print(checkRoute(arr, r_x, r_y, b_x, b_y, cnt))