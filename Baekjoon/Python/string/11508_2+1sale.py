N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

answer = 0
arr.sort(reverse = True)
for i in range(len(arr)):
    if (i % 3) != 2:
        answer += arr[i]

print(answer)