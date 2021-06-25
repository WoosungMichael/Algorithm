num = input()
answer = int(num[0])
for i in range(len(num)-1):
    if(answer <= 1 or int(num[i+1]) <= 1):
        answer += int(num[i+1])
    else:
        answer *= int(num[i+1])

print(answer)
