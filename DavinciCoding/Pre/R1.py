from itertools import combinations
import copy

N, C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

arr = sorted(arr)
arr_t = copy.deepcopy(arr)
if(C == 2):
    max = arr[1]-arr[0]

else:
    del arr_t[-1]
    del arr_t[0]
    list1 = list(combinations(arr, C-2))
    max = 0
    for i in list1:
        i = list(i)
        i.append(arr[0])
        i.append(arr[-1])
        i = sorted(i)
        list2 = list(combinations(i, 2))
        min = list2[0][1]-list2[0][0]
        for j in list2:
            if(j[1]-j[0] < min):
                min = j[1]-j[0]

        if(min > max):
            max = min

print(max)
