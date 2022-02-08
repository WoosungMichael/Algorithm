N = int(input())

cnt = 0
for i in range(60):
    for j in range(60):
        if "3" in str(i) + str(j):
            cnt += 1

answer = 0
for i in range(N + 1):
    if "3" in str(i):
        answer += 3600
    else:
        answer += cnt

print(answer)

'''
N = int(input())

H, M, S = 0, 0, 0
cnt = 0

while True:
    if ("3" in str(H) or "3" in str(M) or "3" in str(S)):
        cnt += 1
    if H == N and M == 59 and S == 59:
        break
    
    S += 1
    if S == 60:
        S = 0
        M += 1
    if M == 60:
        M = 0
        H += 1

print(cnt)
'''