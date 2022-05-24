T = int(input())
for i in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0 for i in range(M + 1)]
    dp[0] = 1
    for i in coin:
        for j in range(1, M + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[-1])