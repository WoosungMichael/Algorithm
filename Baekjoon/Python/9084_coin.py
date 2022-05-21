# from collections import deque

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     coin = list(map(int, input().split()))
#     price = int(input())

#     q = deque()

#     arr = [[0, 0] for _ in range(price + 1)]
#     for i in coin:
#         arr[i][0] = 1
#         q.append([i, 0])

#     while q:
#         index, tmp = q.popleft()
#         for j in coin:
#             if index + j <= price and tmp <= j:
#                 arr[index + j][0] += arr[index][0]
#                 q.append([index + j, j])

#     print(arr[-1][0])
#     print(len(arr))

#     #2원, 3원으로 5원 만드는 가지 수 : 1 아닐까

t = int(input())
for i in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())
    dp = [0 for i in range(m + 1)]
    dp[0] = 1
    for i in c:
        for j in range(1, m + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp)