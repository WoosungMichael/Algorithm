T = int(input())

for i in range(T):
    n = int(input())
    arr = [1, 1, 1, 2, 2]
    if n < 6:
        print(arr[n - 1])
    else:
        for j in range(5, n):
            arr.append(arr[-1] + arr[-5])
        print(arr[-1])