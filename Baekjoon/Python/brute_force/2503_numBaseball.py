import itertools


def ball_cnt(a, b):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                continue
            elif a[i] == b[j]:
                cnt += 1
    return cnt


def strike_cnt(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    return cnt


N = int(input())

arr = []
for i in range(N):
    num, s, b = map(int, input().split())
    arr.append([num, s, b])

num_arr = []
for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3):
    num_arr.append(str(i[0]*100+i[1]*10+i[2]))


cnt = 0
for i in num_arr:
    flag = True
    for j in arr:
        if(strike_cnt(i, str(j[0])) != j[1] or ball_cnt(i, str(j[0])) != j[2]):
            flag = False
    if flag:
        cnt += 1

print(cnt)
