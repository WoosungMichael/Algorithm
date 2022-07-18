def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
    
N = int(input())
answer = 0
if N <= 1:
    print(0)
else:
    num = factorial(N)
    while num % 10 == 0:
        answer += 1
        num //= 10
    print(answer)