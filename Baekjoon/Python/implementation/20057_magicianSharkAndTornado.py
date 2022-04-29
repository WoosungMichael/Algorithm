N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

position = [N // 2, N // 2]

def tornado(position, i, arr, N, dx, dy):
    out = 0
    tmp = 0
    if 0 <= position[0] + dx[(i + 3) % 4] < N and 0 <= position[1] + dy[(i + 3) % 4] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.01)
        arr[position[0] + dx[(i + 3) % 4]][position[1] + dy[(i + 3) % 4]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.01)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.01)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.01)

    if 0 <= position[0] + dx[(i + 1) % 4] < N and 0 <= position[1] + dy[(i + 1) % 4] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.01)
        arr[position[0] + dx[(i + 1) % 4]][ position[1] + dy[(i + 1) % 4]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.01)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.01)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.01)

    if 0 <= position[0] + dx[i] + dx[(i + 3) % 4] < N and 0 <= position[1] + dy[i] + dy[(i + 3) % 4] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.07)
        arr[position[0] + dx[i] + dx[(i + 3) % 4]][position[1] + dy[i] + dy[(i + 3) % 4]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.07)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.07)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.07)

    if 0 <= position[0] + dx[i] + dx[(i + 1) % 4] < N and 0 <= position[1] + dy[i] + dy[(i + 1) % 4] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.07)
        arr[position[0] + dx[i] + dx[(i + 1) % 4]][position[1] + dy[i] + dy[(i + 1) % 4]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.07)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.07)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.07)

    if 0 <= position[0] + dx[i] + 2 * dx[(i + 3) % 4] < N and 0 <= position[1] + dy[i] + 2 * dy[(i + 3) % 4] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.02)
        arr[position[0] + dx[i] + 2 * dx[(i + 3) % 4]][position[1] + dy[i] + 2 * dy[(i + 3) % 4]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.02)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.02)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.02)

    if 0 <= position[0] + dx[i] + 2 * dx[(i + 1) % 4] < N and 0 <= position[1] + dy[i] + 2 * dy[(i + 1) % 4] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.02)
        arr[position[0] + dx[i] + 2 * dx[(i + 1) % 4]][position[1] + dy[i] + 2 * dy[(i + 1) % 4]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.02)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.02)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.02)

    if 0 <= position[0] + 2 * dx[i] + dx[(i + 3) % 4] < N and 0 <= position[1] + 2 * dy[i] + dy[(i + 3) % 4] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.1)
        arr[position[0] + 2 * dx[i] + dx[(i + 3) % 4]][position[1] + 2 * dy[i] + dy[(i + 3) % 4]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.1)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.1)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.1)

    if 0 <= position[0] + 2 * dx[i] + dx[(i + 1) % 4] < N and 0 <= position[1] + 2 * dy[i] + dy[(i + 1) % 4] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.1)
        arr[position[0] + 2 * dx[i] + dx[(i + 1) % 4]][position[1] + 2 * dy[i] + dy[(i + 1) % 4]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.1)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.1)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.1)

    if 0 <= position[0] + 3 * dx[i] < N and 0 <= position[1] + 3 * dy[i] < N:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.05)
        arr[position[0] + 3 * dx[i]][position[1] + 3 * dy[i]] += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.05)
    else:
        tmp += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.05)
        out += int(arr[position[0] + dx[i]][position[1] + dy[i]] * 0.05)

    if 0 <= position[0] + 2 * dx[i] < N and 0 <= position[1] + 2 * dy[i] < N:
        arr[position[0] + 2 * dx[i]][position[1] + 2 * dy[i]] += arr[position[0] + dx[i]][position[1] + dy[i]] - tmp
    else:
        out += arr[position[0] + dx[i]][position[1] + dy[i]] - tmp

    arr[position[0] + dx[i]][position[1] + dy[i]] = 0

    return arr, out

move = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0] #좌하우상 / 반시계방향 : +1
flag = False
answer = 0
while True:
    move += 1
    for i in range(4):
        for j in range(move):
            if position == [0, 0]:
                flag = True
                break
            else:
                arr, out = tornado(position, i, arr, N, dx, dy)
                answer += out
                position = [position[0] + dx[i], position[1] + dy[i]]

        if flag:
            break
        if i == 1:
            move += 1
    if flag:
        break

print(answer)