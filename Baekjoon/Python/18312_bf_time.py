N, K = map(int, input().split())

cnt = 0
for i in range(0, N+1):
    if(i < 10):
        s_i = "0" + str(i)
    else:
        s_i = str(i)
    if(str(K) in s_i):
        cnt += 3600
        continue
    for j in range(0, 60):
        if(j < 10):
            s_j = "0" + str(j)
        else:
            s_j = str(j)
        if(str(K) in s_j):
            cnt += 60
            continue
        for k in range(0, 60):
            if(k < 10):
                s_k = "0" + str(k)
            else:
                s_k = str(k)
            if(str(K) in s_k):
                cnt += 1

print(cnt)
