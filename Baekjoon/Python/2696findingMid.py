T = int(input())

for i in range(T):
    M = int(input())
    arr = []
    for j in range((M//10)+1):
        arr.extend(list(map(int, input().split())))

    print((M+1)//2)
    arr1 = []
    cnt = 0
    for j in range(M):
        arr1.append(arr[j])
        arr1.sort()
        if(j % 2 == 0):
            cnt += 1
            print(arr1[j//2], end=" ")
            if(cnt % 10 == 0 or j == M-1):
                print()
