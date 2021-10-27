N = int(input())

arr = []
for i in range(N):
    tmp = input()
    flag = False
    tmp_w = ""
    for j in tmp:
        if flag:
            tmp_w += j
        if j == '.':
            flag = True
    arr.append(tmp_w)

arr.sort()

cnt = 1
flag = True
for i in range(len(arr)):
    if flag:
        print(arr[i], end=" ")
        flag = False
    if i == len(arr)-1 or arr[i] != arr[i+1]:
        print(cnt)
        cnt = 1
        flag = True
    else:
        cnt += 1
