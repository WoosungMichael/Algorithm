N = int(input())
arr = []
min = 1000000000
max = 0

for i in range(N):
    a, b, c = (map(int, input().split()))
    for j in range(a, c+1):
        arr.append([j, b])

    if(a < min):
        min = a
    elif(c > max):
        max = c

for i in range(max+2):
    arr.append([i, 0])

arr.sort(key=lambda x: (x[0], -x[1]))

i_x = -1
i_y = -1
for i in range(len(arr)):
    if(i_y != arr[i][1] and i_x != arr[i][0]):
        if(i_y < arr[i][1]):
            print(arr[i][0], arr[i][1])
        else:
            print(arr[i][0]-1, arr[i][1])
        i_x = arr[i][0]
        i_y = arr[i][1]
    else:
        i_x = arr[i][0]
