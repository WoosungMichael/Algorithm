import sys
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    tmp = input().rstrip()
    stack = []
    for j in tmp:
        if j == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        else:
            stack.append('(')
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
