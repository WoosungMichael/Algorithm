N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()
arr = arr[::-1]

cost = 0

for i in range(len(arr)):
    if(arr[i]-i > 0):
        cost += arr[i]-i

print(cost)
