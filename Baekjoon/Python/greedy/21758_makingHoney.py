N = int(input())
arr = list(map(int, input().split()))

arr_left = []
arr_right = []

tmp = 0
for i in range(N):
    tmp += int(arr[i])
    arr_right.append(tmp)

tmp = 0
for i in reversed(range(N)):
    tmp += arr[i]
    arr_left.append(tmp)
arr_left.reverse()

tmp = 0
for i in range(1, N-1):
    if tmp < arr_left[i] + arr_right[i] - arr[0] - arr[-1]:
        tmp = arr_left[i] + arr_right[i] - arr[0] - arr[-1]

# 벌통 왼쪽
for i in range(1, N-1):
    if tmp < arr_right[-1] - arr[-1] - 2 * arr[i] + arr_right[i]:
        tmp = arr_right[-1] - arr[-1] - 2 * arr[i] + arr_right[i]

# 벌통 오른쪽
for i in range(1, N-1):
    if tmp < arr_left[0] - arr[0] - 2 * arr[i] + arr_left[i]:
        tmp = arr_left[0] - arr[0] - 2 * arr[i] + arr_left[i]

print(tmp)
