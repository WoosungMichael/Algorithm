N = int(input())

arr = [2 for i in range(10)]
cnt = 0
for i in range(N):
    c, p = map(int, input().split())
    if arr[c - 1] == 2:
        arr[c - 1] = p
    else:
        if arr[c - 1] != p:
            cnt += 1
            arr[c - 1] = p

print(cnt)