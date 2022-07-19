N = int(input())

arr = list(map(int, input().split()))
ring = arr[0]

for i in range(1, len(arr)):
    print("", end = "")
    print("/", end = "")
    print("", end = "")
    