N, x = map(int, input().split())
list = list(map(int, input().split()))

cnt = 0
for i in list:
    if(i == x):
        cnt += 1
    elif(i > x):
        break

if(cnt > 0):
    print(cnt)
else:
    print(-1)
