N, M = map(int, input().split())

max = 0
for i in range(N):
    min = 100
    tmp = list(map(int, input().split()))
    for i in tmp:
        if min > i:
            min = i
    if max < min:
        max = min

print(max)