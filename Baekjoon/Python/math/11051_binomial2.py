N, K = map(int, input().split())

answer = 1
if K < 0 or N < 0 or K > N:
    print(0)
else:
    for i in range(N, N - K, -1):
        answer *= i
    for i in range(1, K + 1):
        answer //= i
    print(answer % 10007)