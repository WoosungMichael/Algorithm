N = int(input())

cnt = 0
for i in range(N):
    line = input()
    stack = []
    for j in line:
        if len(stack) != 0 and stack[-1] == j:
            stack.pop()
        else:
            stack.append(j)
    if len(stack) == 0:
        cnt += 1
print(cnt)