line = input()

stack = []
cnt = 0
for i in range(len(line) - 1):
    if line[i] == '(':
        if line[i + 1] == ')':
            cnt += len(stack)
        else:
            stack.append('(')
    else:
        if line[i - 1] != '(':
            stack.pop()
            cnt += 1

cnt += len(stack)
print(cnt)