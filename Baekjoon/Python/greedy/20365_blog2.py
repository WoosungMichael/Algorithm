N = int(input())
str = input()

tmp = str[0]
cnt = 1
flag = 1
for i in str:
    if i != tmp:
        if(flag == 1):
            cnt += 1
            flag = 0
    else:
        flag = 1

print(cnt)
