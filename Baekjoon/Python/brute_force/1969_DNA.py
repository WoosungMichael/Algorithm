from collections import Counter

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(input())

str = ""
for i in range(M):
    tmp = []
    for j in range(N):
        tmp.append(arr[j][i])
    mc = Counter(tmp)
    val = mc.most_common(1)[0][1]
    tmp2 = []
    for j in mc.most_common():
        if j[1] == val:
            tmp2.append(j[0])
    tmp2.sort()
    str += tmp2[0]


cnt = 0
for i in range(M):
    for j in range(N):
        if(arr[j][i] != str[i]):
            cnt += 1

print(str)
print(cnt)
