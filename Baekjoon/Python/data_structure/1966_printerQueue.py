from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    i_list = deque(map(int, input().split()))
    flag = deque()
    for j in range(N):
        if j != M:
            flag.append(0)
        else:
            flag.append(1)

    cnt = 0
    while True:
        if i_list[0] == max(i_list):
            if flag[0] == 0:
                i_list.popleft()
                flag.popleft()
                cnt += 1
            else:
                cnt += 1
                print(cnt)
                break
        else:
            i_list.append(i_list[0])
            if flag[0] == 0:
                flag.append(0)
            else:
                flag.append(1)
            i_list.popleft()
            flag.popleft()