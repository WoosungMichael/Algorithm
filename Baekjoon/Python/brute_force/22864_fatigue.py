A, B, C, M = map(int, input().split())

fatigue = 0
answer = 0
for _ in range(24):
    if fatigue + A > M:
        fatigue = max(0, fatigue - C)
    else:
        fatigue += A
        answer += B

print(answer)