from itertools import permutations

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(i + 1)
arr_list = list(permutations(arr, M))

for i in arr_list:
    for j in i:
        print(j, end=" ")
    print()

# 백트래킹 풀이로 다시 풀어보기!
