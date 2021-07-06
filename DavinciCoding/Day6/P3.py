x, y = map(int, input().split())
arr = []
for i in range(x):
    arr.append(list(map(int, input().split())))
n = int(input())

min = n*n+1
for i in range(x-n+1):
    for j in range(y-n+1):
        flag = False
        cnt = 0
        for k in range(i, i+n):
            for l in range(j, j+n):
                if(arr[k][l] == 2):
                    flag = True
                    break
                elif(arr[k][l] == 1):
                    cnt += 1

            if(flag == True):
                cnt = n*n+1
                break

        if(cnt < min):
            min = cnt

if(min == n*n+1):
    min = -1

print(min)
