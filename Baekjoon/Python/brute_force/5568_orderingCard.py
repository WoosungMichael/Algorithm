from itertools import permutations

n = int(input())
k = int(input())

arr = []
for i in range(n):
    arr.append(input())

arr_list = list(permutations(arr, k))

sort_list = []
for i in arr_list:
    tmp = ""
    for j in i:
        tmp += j
    sort_list.append(tmp)

print(len(set(sort_list)))
