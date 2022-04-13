N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

if N <= 2:
    tmp = 0
    for i in range(N):
        tmp += arr[i]
    print(tmp)
    exit()

sum = [arr[0], arr[0] + arr[1], max(arr[0], arr[1]) + arr[2]]
for i in range(3, N):
    sum.append(max(sum[i - 2], sum[i - 3] + arr[i - 1]) + arr[i])

print(sum[N - 1])