import random

N = int(input())

arr = [i+1 for i in range(N)]
random.shuffle(arr)

for i in arr:
    print(i, end=" ")
