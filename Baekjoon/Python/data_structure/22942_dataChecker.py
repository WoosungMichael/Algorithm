import sys
input = sys.stdin.readline
N = int(input().rstrip())

data = {}
for i in range(N):
    o, r = map(int, input().split())
    data[o - r] = i
    data[o + r] = i

data = sorted(data.items())
tmp = []
for i in data:
    if len(tmp) != 0 and tmp[-1] == i[1]:
        tmp.pop()
    else:
        tmp.append(i[1])
if len(tmp) == 0:
    print("YES")
else:
    print("NO")