from collections import deque

N = int(input())
arr = deque()
for i in range(N):
    arr.append(i+1)

while len(arr)!=1:
    arr.popleft()
    arr.append(arr.popleft())
print(arr[0])
    