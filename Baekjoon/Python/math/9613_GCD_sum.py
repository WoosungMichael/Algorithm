import math

t = int(input())

for n in range(t):
    arr = list(map(int, input().split()))
    arr.pop(0)
    sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum += math.gcd(arr[i], arr[j])
    print(sum)
