N, M = map(int, input().split())
bulb = list(map(int, input().split()))

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        bulb[b - 1] = c
    elif a == 2:
        for j in range(b - 1, c):
            if bulb[j] == 0:
                bulb[j] = 1
            else:
                bulb[j] = 0
    elif a == 3:
        for j in range(b - 1, c):
            bulb[j] = 0
    elif a == 4:
        for j in range(b - 1, c):
            bulb[j] = 1

for i in bulb:
    print(i, end = " ")