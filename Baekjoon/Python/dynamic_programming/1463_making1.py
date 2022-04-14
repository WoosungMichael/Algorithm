N = int(input())

arr = [0, 0]

for i in range(2, N + 1):
    tmp = arr[i - 1] + 1
    if i % 3 == 0:
        if tmp > arr[i // 3] + 1:
            tmp = arr[i // 3] + 1
    if i % 2 == 0:
        if tmp > arr[i // 2] + 1:
            tmp = arr[i // 2] + 1
    arr.append(tmp)

print(arr[-1])