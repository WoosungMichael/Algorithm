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

cnt = 0
for i in range(123, 1000):
    num_s = str(i)
    if(num_s[0] == 0 or num_s[1] == 0 or num_s[2] == 0 or num_s[0] == num_s[1] or num_s[0] == num_s[2] or num_s[1] == num_s[2]):
        continue
    flag = True
    for j in arr:
        if(strike_cnt(num_s, str(j[0])) != j[1] or ball_cnt(num_s, str(j[0])) != j[2]):
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)
