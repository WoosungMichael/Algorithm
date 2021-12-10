N = int(input())

flag = True
n = 2
while N > 1:
    if N % n == 0:
        print(n)
        N = N/n
    else:
        n += 1
