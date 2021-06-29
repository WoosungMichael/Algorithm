N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

print(arr)
max = 0
for i in arr:
    if(max < min(i)):
        max = min(i)

print(max)
