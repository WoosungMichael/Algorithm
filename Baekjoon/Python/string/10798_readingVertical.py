arr = [[-1 for i in range(15)] for j in range(5)]

for i in range(5):
    str = input()
    for j in range(len(str)):
        arr[i][j] = str[j]

for y in range(15):
    for x in range(5):
        if arr[x][y] != -1:
            print(arr[x][y], end="")
