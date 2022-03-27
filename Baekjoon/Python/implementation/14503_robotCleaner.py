def checkWall(arr, r, c, N, M):
    if 0 <= r and r < N and 0 <= c and c < M:
        if arr[r][c] != 1:
            return True
        return False
    return False

def checkSquare(cnt, arr, r, c, d, N, M):
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    if d == 0:
        if c - 1 >= 0 and arr[r][c - 1] == 0:
            return [cnt, r, c - 1, 3]
        if r + 1 < N and arr[r + 1][c] == 0:
            return [cnt, r + 1, c, 2]
        if c + 1 < M and arr[r][c + 1] == 0:
            return [cnt, r, c + 1, 1]
        if r - 1 >= 0 and arr[r - 1][c] == 0:
            return [cnt, r - 1, c, 0]
        if r + 1 < N:
            if checkWall(arr, r + 1, c, N, M):
                return [cnt, r + 1, c, 0]
            else:
                return [cnt, -1, -1, -1]
    elif d == 1:
        if r - 1 >= 0 and arr[r - 1][c] == 0:
            return [cnt, r - 1, c, 0]
        if c - 1 >= 0 and arr[r][c - 1] == 0:
            return [cnt, r, c - 1, 3]
        if r + 1 < N and arr[r + 1][c] == 0:
            return [cnt, r + 1, c, 2]
        if c + 1 < M and arr[r][c + 1] == 0:
            return [cnt, r, c + 1, 1]
        if c - 1 >= 0:
            if checkWall(arr, r, c - 1, N, M):
                return [cnt, r, c - 1, 1]
            else:
                return [cnt, -1, -1, -1]
    elif d == 2:
        if c + 1 < M and arr[r][c + 1] == 0:
            return [cnt, r, c + 1, 1]
        if r - 1 >= 0 and arr[r - 1][c] == 0:
            return [cnt, r - 1, c, 0]
        if c - 1 >= 0 and arr[r][c - 1] == 0:
            return [cnt, r, c - 1, 3]
        if r + 1 < N and arr[r + 1][c] == 0:
            return [cnt, r + 1, c, 2]
        if r - 1 >= 0:
            if checkWall(arr, r - 1, c, N, M):
                return [cnt, r - 1, c, 2]
            else:
                return [cnt, -1, -1, -1]
    else:
        if r + 1 < N and arr[r + 1][c] == 0:
            return [cnt, r + 1, c, 2]
        if c + 1 < M and arr[r][c + 1] == 0:
            return [cnt, r, c + 1, 1]
        if r - 1 >= 0 and arr[r - 1][c] == 0:
            return [cnt, r - 1, c, 0]
        if c - 1 >= 0 and arr[r][c - 1] == 0:
            return [cnt, r, c - 1, 3]
        if c + 1 >= 0:
            if checkWall(arr, r, c + 1, N, M):
                return [cnt, r, c + 1, 3]
            else:
                return [cnt, -1, -1, -1]
    return [cnt, -1, -1, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    cnt, r, c, d = checkSquare(cnt, arr, r, c, d, N, M)
    if d == -1:
        break
print(cnt)