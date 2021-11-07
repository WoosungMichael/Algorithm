from itertools import product

N, K = map(int, input().split())
arr = list(input().split())

for i in reversed(range(int(K)+1)):
    tmp = list(product(arr, repeat=i))
    tmp.sort(reverse=True)
    for i in tmp:
        if int("".join(i)) <= N:
            print(int("".join(i)))
            exit()
