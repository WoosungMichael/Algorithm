import sys
input = sys.stdin.readline

N = int(input().rstrip())
stack = []

for i in range(N):
    cmd = input().rstrip()
    tmp = cmd.split()
    if " " in cmd:
        stack.append(tmp[1])
    else:
        if cmd == "top":
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)
        elif cmd == "size":
            print(len(stack))
        elif cmd == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif cmd == "pop":
            if len(stack) != 0:
                print(stack[-1])
                stack.pop()
            else:
                print(-1)
