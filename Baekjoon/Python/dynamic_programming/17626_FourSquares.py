n = int(input())
arr = [0, 1]

for i in range(2, n + 1):
    tmp = i
    if i == int(i ** 0.5) ** 2:
        tmp = 1
    else:
        for j in range(1, int(i ** 0.5) + 1):
            if arr[i - j ** 2] == 1:
                tmp = 2
                break
            if arr[i - j ** 2] + 1 < tmp:
                tmp = arr[i - j ** 2] + 1
    arr.append(tmp)

print(arr[-1])
    