N = int(input())
d = list(map(int, input().split()))
arr = list(map(int, input().split()))

cost = 0
tmp = arr[0]
dist = 0

for i in range(1, len(arr)):
    dist += d[i-1]
    if(tmp > arr[i]):
        cost += tmp*dist
        tmp = arr[i]
        dist = 0

cost += tmp*dist

print(cost)
