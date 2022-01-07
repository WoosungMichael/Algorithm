import sys
input = sys.stdin.readline

N = int(input())

arr = []
init = 0
for i in range(N):
    cmd = input().strip()
    if " " in cmd:
        tmp = cmd.split()
        arr.append(tmp[-1])
    elif cmd == "front":
        if len(arr) > init:
            print(arr[init])
        else:
            print(-1)
    elif cmd == "back":
        if len(arr) > init:
            print(arr[-1])
        else:
            print(-1)
    elif cmd == "size":
        print(len(arr)-init)
    elif cmd == "empty":
        if len(arr) == init:
            print(1)
            init = 0
            arr = []
        else:
            print(0)
    elif cmd == "pop":
        if len(arr) != init:
            print(arr[init])
            init += 1
        else:
            print(-1)