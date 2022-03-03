import sys
input = sys.stdin.readline

n = int(input().rstrip())
fibo = []

for i in range(n + 1):
    if i == 0:
        fibo.append(0)
    elif i == 1:
        fibo.append(1)
    else:
        fibo.append(fibo[i - 2] + fibo[i - 1])

print(fibo[n])