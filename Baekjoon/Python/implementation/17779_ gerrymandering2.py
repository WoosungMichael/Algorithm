N = int(input())

arr = [[0] * (N + 1)]
for i in range(N):
    arr1 = [0]
    tmp = list(map(int, input().split()))
    for j in tmp:
        arr1.append(j)
    arr.append(arr1)

def countGap(x, y, d1, d2):
    cnt = [0, 0, 0, 0, 0]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i - x + y - 2 * d1 <= j and j <= i - x + y and -i + x + y <= j and j <= -i + x + y + 2 * d2:
                cnt[4] += arr[i][j]
            elif i < x + d1 and j <= y:
                cnt[0] += arr[i][j]
            elif i <= x + d2 and y < j:
                cnt[1] += arr[i][j]
            elif x + d1 <= i and j < y - d1 + d2:
                cnt[2] += arr[i][j]
            elif x + d2 < i and y - d1 + d2 <= j:
                cnt[3] += arr[i][j]
    return max(cnt) - min(cnt)

global_min = 2000

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N - i):
            for l in range(1, N - j):
                if i + k + l <= N - 1 and 0 <= j - k and j + l <= N - 1:
                    tmp_min = countGap(i, j, k, l)
                    if tmp_min < global_min:
                        global_min = tmp_min

print(global_min)