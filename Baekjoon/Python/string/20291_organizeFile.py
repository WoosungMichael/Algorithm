N = int(input())

arr = dict()
for i in range(N):
    tmp = input().split('.')[1]
    if tmp not in arr:
        arr[tmp] = 1
    else:
        arr[tmp] += 1

sorted_arr = sorted(arr.items())


for key, value in sorted_arr:
    print(key, value)
