k = int(input())
food_times = list(map(int, input().split()))


if(sum(food_times) <= k):
    answer = -1
else:
    arr = []
    for i in range(len(food_times)):
        arr.append([i, food_times[i]])

    minnum = min(food_times)
    f_len = len(food_times)
    while k >= minnum*f_len:
        k -= minnum*f_len
        i = 0
        while i < len(arr):
            arr[i][1] -= minnum
            if(arr[i][1] == 0):
                del(arr[i])
                i -= 1
            i += 1
        minnum = 1000
        for i in arr:
            if(i[1] < minnum):
                minnum = i[1]
        f_len = len(arr)
    answer = arr[k % f_len][0]+1

print(answer)
