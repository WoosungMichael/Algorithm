T = int(input())

for i in range(T):
    N = int(input())
    min = 1000001
    max = -1000001
    tmp = list(map(int, input().split()))
    for j in tmp:
        if j > max:
            max = j
        if j < min:
            min = j
    print(min, end = " ")
    print(max)