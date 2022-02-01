A, B, C = map(int, input().split())

answer = 1
flag = True
arr = [A, B, C]
for i in arr:
    if i % 2 == 1:
        answer *= i
        flag = False

if flag == True:
    answer = A * B * C

print(answer)