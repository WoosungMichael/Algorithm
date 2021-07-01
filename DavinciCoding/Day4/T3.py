N, len = map(int, input().split())

list = []
for i in range(N):
    list.append(int(input()))

init = max(list)

while True:
    cnt = 0
    for i in list:
        if(i > init):
            cnt += i-init

    if(cnt >= len):
        print(init)
        break
    else:
        init -= 1
