n = int(input())

cnt = 0
stack = []
output = []
msg=True

for i in range(0,n):
    x = int(input())

    while cnt < x:
      cnt += 1
      output.append("+")
      stack.append(cnt)

    if stack[-1]==x:
        output.append("-")
        stack.pop()
    else:
        msg = False

if msg==False:
    print("NO")
else:
    print("\n".join(output))