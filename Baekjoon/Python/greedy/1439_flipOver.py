S = input()

start = S[0]
cnt = 0
for i in S:
    if i != start:
        start = i
        cnt += 1

print((cnt + 1) // 2)