N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
c_time = 0
for i in arr:
    if c_time <= i[0]:
        cnt += 1
        c_time = i[1]
print(cnt)
