from collections import deque
import sys
input = sys.stdin.readline
arr = deque()

N = int(input().rstrip())
for i in range(N):
    tmp = input().split()
    
    if tmp[0] == "push_back":
        arr.append(tmp[1])
    elif tmp[0] == "push_front":
        arr.appendleft(tmp[1])
    elif tmp[0] == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif tmp[0] == "back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif tmp[0] == "size":
        print(len(arr))
    elif tmp[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == "pop_front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
            arr.popleft()
    elif tmp[0] == "pop_back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
            arr.pop()
