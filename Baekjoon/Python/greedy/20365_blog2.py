N = int(input())
str = input()

cnt_B = 0
cnt_R = 0
tmp = 'a'
for i in str:
    if i == 'B' and tmp != 'B':
        cnt_B += 1
        tmp = 'B'
    elif i == 'R' and tmp != 'R':
        cnt_R += 1
        tmp = 'R'

if cnt_B > cnt_R:
    tmp = 'B'
else:
    tmp = 'R'
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
