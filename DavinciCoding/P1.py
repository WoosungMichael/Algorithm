cost = int(input())
arr = list(map(int, input().split()))

max = 0
for i in range(len(arr)-1):
    sum = 0
    cnt = 0
    for j in range(i, len(arr)):
        if sum+arr[j] <= cost:
            sum += arr[j]
            cnt += 1
        else:
            break
    if(max < cnt):
        max = cnt

print(max)
