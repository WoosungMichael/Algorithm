N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

max = 0
for i in range(len(arr)):
    min = arr[i][0]
    for j in arr[i]:
        if(j < min):
            min = j
    if(max < min):
        max = min

print(max)
