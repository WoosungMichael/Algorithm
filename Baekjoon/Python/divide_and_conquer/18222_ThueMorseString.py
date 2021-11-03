import copy
k = int(input())
cnt = 0

while k > 2:
    i = 0
    tmp = copy.deepcopy(k-1)
    while tmp > 1:
        tmp //= 2
        i += 1

    i = 2 ** i
    k -= i
    cnt += 1

if (k == 1 and cnt % 2 == 0) or (k == 2 and cnt % 2 == 1):
    print(0)
elif (k == 2 and cnt % 2 == 0) or (k == 1 and cnt % 2 == 1):
    print(1)
