import math
N = int(input())
arr = map(int, input().split())
x = int(input())

tmp = []
for i in arr:
    if math.gcd(i, x) == 1:
        tmp.append(i)

print(sum(tmp)/len(tmp))
