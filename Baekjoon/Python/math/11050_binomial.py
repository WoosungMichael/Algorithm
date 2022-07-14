def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

N, K = map(int, input().split())

answer = 1
if K < 0 or N < 0 or K > N:
    print(0)
else:
    answer *= factorial(N)
    answer /= factorial(K)
    answer /= factorial(N - K)
    print(int(answer))