n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

answer = [-1] * (k + 1)
for i in arr:
    if i <= k:
        answer[i] = 1

print(answer)

for i in range(1, k + 1):
    for j in arr:
        if i - j > 0 and answer[i - j] != -1:
            if answer[i] == -1:
                answer[i] = answer[i - j] + 1
            else:
                if answer[i - j] + 1 < answer[i]:
                    answer[i] = answer[i - j] + 1

print(answer[k])