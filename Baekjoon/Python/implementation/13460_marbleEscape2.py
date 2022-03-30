def moveUp(arr, r_x, r_y, b_x, b_y, cnt):
    tmp = r_x
    flag_r = False
    for i in range(r_x - 1, 0, -1):
        if arr[i][r_y] == '.':
            tmp = i
        elif arr[i][r_y] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[i][r_y] == '0':
            arr[tmp][r_y] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp][r_y] = 'R'
    r_x = tmp

    tmp = b_x
    flag_b = False
    for i in range(b_x - 1, 0, -1):
        if arr[i][b_y] == '.':
            tmp = i
        elif arr[i][b_y] == '#' or arr[i][b_y] == 'R':
            break
        elif arr[i][b_y] == '0':
            arr[tmp][b_y] = '.'
            flag_b = True
            break
    arr[b_x][b_y] = '.'
    if not flag_b:
       arr[tmp][b_y] = 'B'
    b_x = tmp

    for i in range(r_x - 1, 0, -1):
        if arr[i][r_y] == '.':
            tmp = i
        elif arr[i][r_y] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[i][r_y] == '0':
            arr[tmp][r_y] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp][r_y] = 'R'
    r_x = tmp

    return r_x, r_y, b_x, b_y, flag_r, flag_b

def moveDown(arr, r_x, r_y, b_x, b_y, cnt):
    tmp = r_x
    flag_r = False
    for i in range(r_x + 1, N):
        if arr[i][r_y] == '.':
            tmp = i
        elif arr[i][r_y] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[i][r_y] == '0':
            arr[tmp][r_y] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp][r_y] = 'R'
    r_x = tmp

    tmp = b_x
    flag_b = False
    for i in range(b_x + 1, N):
        if arr[i][b_y] == '.':
            tmp = i
        elif arr[i][b_y] == '#' or arr[i][b_y] == 'R':
            break
        elif arr[i][b_y] == '0':
            arr[tmp][b_y] = '.'
            flag_b = True
            break
    arr[b_x][b_y] = '.'
    if not flag_b:
        arr[tmp][b_y] = 'B'
    b_x = tmp

    for i in range(r_x + 1, N):
        if arr[i][r_y] == '.':
            tmp = i
        elif arr[i][r_y] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[i][r_y] == '0':
            arr[tmp][r_y] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp][r_y] = 'R'
    r_x = tmp

    return r_x, r_y, b_x, b_y, flag_r, flag_b
    
def moveLeft(arr, r_x, r_y, b_x, b_y, cnt):
    tmp = r_y
    flag_r = False
    for i in range(r_y - 1, 0, -1):
        if arr[r_x][i] == '.':
            tmp = i
        elif arr[r_x][i] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[r_x][i] == '0':
            arr[r_x][tmp] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp][r_y] = 'R'
    r_y = tmp

    tmp = b_y
    flag_b = False
    for i in range(b_y - 1, 0, -1):
        if arr[b_x][i] == '.':
            tmp = i
        elif arr[b_x][i] == '#' or arr[i][b_y] == 'R':
            break
        elif arr[b_x][i] == '0':
            arr[b_x][tmp] = '.'
            flag_b = True
            break
    arr[b_x][b_y] = '.'
    if not flag_b:
        arr[tmp][b_y] = 'B'
    b_y = tmp

    for i in range(r_y - 1, 0, -1):
        if arr[r_x][i] == '.':
            tmp = i
        elif arr[r_x][i] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[r_x][i] == '0':
            arr[r_x][tmp] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp][r_y] = 'R'
    r_y = tmp

    return r_x, r_y, b_x, b_y, flag_r, flag_b
    
def moveRight(arr, r_x, r_y, b_x, b_y, cnt):
    tmp = r_y
    flag_r = False
    for i in range(r_y + 1, M):
        if arr[r_x][i] == '.':
            tmp = i
        elif arr[r_x][i] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[r_x][i] == '0':
            arr[r_x][tmp] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp][r_y] = 'R'
    r_y = tmp

    tmp = b_y
    flag_b = False
    for i in range(b_x + 1, M):
        if arr[b_x][i] == '.':
            tmp = i
        elif arr[b_x][i] == '#' or arr[i][b_y] == 'R':
            break
        elif arr[b_x][i] == '0':
            arr[b_x][tmp] = '.'
            flag_r = True
            break
    arr[b_x][b_y] = '.'
    if not flag_b:
        arr[tmp][b_y] = 'B'
    b_y = tmp

    for i in range(r_y + 1, M):
        if arr[r_x][i] == '.':
            tmp = i
        elif arr[r_x][i] == '#' or arr[i][r_y] == 'B':
            break
        elif arr[r_x][i] == '0':
            arr[r_x][tmp] = '.'
            flag_r = True
            break
    arr[r_x][r_y] = '.'
    if not flag_r:
        arr[tmp][r_y] = 'R'
    r_y = tmp

    return r_x, r_y, b_x, b_y, flag_r, flag_b
    

def checkRoute(arr, r_x, r_y, b_x, b_y, cnt):
    if arr[r_x - 1][r_y] != '#':
        cnt_u = moveUp(arr, r_x, r_y, b_x, b_y, cnt)
    elif arr[r_x + 1][r_y] != '#':
        cnt_d = moveDown(arr, r_x, r_y, b_x, b_y, cnt)
    elif arr[r_x][r_y - 1] != '#':
        cnt_l = moveLeft(arr, r_x, r_y, b_x, b_y, cnt)
    elif arr[r_x][r_y + 1] != '#':
        cnt_r = moveRight(arr, r_x, r_y, b_x, b_y, cnt)
    
    

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

#DFS처리 필요