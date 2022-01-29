from itertools import combinations 

N, K = map(int, input().split())
arr = list(map(int, input().split()))

tmp = []
for i in range(N - 1):
    tmp.append(i)

check = list(combinations(tmp, K - 1))

answer = 300000
print(check)
for i in check:
    sum = 0
    min = arr[0]
    for j in range(len(arr)):
        if j in i:
            max = arr[j]
            sum += max - min
            min = arr[j + 1]
    sum += arr[-1] - min

    if answer > sum:
        answer = sum

print(answer)