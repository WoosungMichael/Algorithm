arr = [1 for i in range(30)]

for i in range(28):
    arr[int(input()) - 1] = 0

for i in range(len(arr)):
    if arr[i] == 1:
        print(i + 1)