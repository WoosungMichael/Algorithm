def div(a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    for i in range(min_num, 0, -1):
        if max_num % i == 0 and min_num % i == 0:
            return a // i, b // i

N = int(input())

arr = list(map(int, input().split()))
ring = arr[0]

for i in range(1, len(arr)):
    x, y = div(ring, arr[i])
    print(x, end = "")
    print("/", end = "")
    print(y)
    