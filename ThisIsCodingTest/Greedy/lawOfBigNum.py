'''
1) sort를 이용한 풀이

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
tmp = 0
sum = 0
while(cnt < M):
    if tmp < K:
        sum += arr[-1]
        tmp += 1
        cnt += 1
    else:
        sum += arr[-2]
        tmp = 0
        cnt += 1

print(sum)
'''


'''
2) sort를 이용하지 않는 풀이

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

max1 = 0
max2 = 0
for i in arr:
    if max1 < i:
        max2 = max1
        max1 = i
    elif max2 < i:
        max2 = i    

cnt = 0
tmp = 0
sum = 0
while(cnt < M):
    if tmp < K:
        sum += max1
        tmp += 1
        cnt += 1
    else:
        sum += max2
        tmp = 0
        cnt += 1

print(sum)
'''

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

max1 = 0
max2 = 0
for i in arr:
    if max1 < i:
        max2 = max1
        max1 = i
    elif max2 < i:
        max2 = i    

sum = (max1 * K + max2) * (M // (K + 1)) + max1 * (M % (K + 1))

print(sum)