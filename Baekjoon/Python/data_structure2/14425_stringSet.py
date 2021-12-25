N, M = map(int, input().split())

S = []
for i in range(N):
    S.append(input())

cnt = 0
for i in range(M):
    if input() in S:
        cnt += 1

print(cnt)
