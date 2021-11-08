from itertools import product

N, K = input().split()
arr = list(input().split())

for i in reversed(range(len(N)+1)):
    tmp = list(product(arr, repeat=i))
    tmp.sort(reverse=True)
    for i in tmp:
        if int("".join(i)) <= int(N):
            print(int("".join(i)))
            exit()
