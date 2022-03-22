N = int(input())

arr = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in range(N):
    tmp = 1
    if arr[i] > B:
        if (arr[i] - B) % C == 0:
            tmp += (arr[i] - B) // C
        else:
            tmp += (arr[i] - B) // C + 1
    cnt += tmp

print(cnt)