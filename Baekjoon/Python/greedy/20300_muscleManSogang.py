N = int(input())
arr = list(map(int, input().split()))
arr.sort()

max = 0
if (len(arr) % 2 == 0):
    for i in range(len(arr)//2):
        if(arr[i]+arr[-(i+1)] > max):
            max = arr[i]+arr[-(i+1)]

else:
    for i in range(len(arr)//2):
        if(arr[i]+arr[-(i+2)] > max):
            max = arr[i]+arr[-(i+2)]
    if(arr[-1] > max):
        max = arr[-1]

print(max)
