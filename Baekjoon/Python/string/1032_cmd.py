N = int(input())
arr = []
for i in range(N):
    arr.append(input())

for i in range(len(arr[0])):
    tmp = len(arr[0])
    tmp1 = arr[0][i]
    for j in arr:
        if j[i] != tmp1:
            tmp1 = "?"
    print(tmp1, end = "")