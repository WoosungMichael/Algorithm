str = input()

tmp = 1
flag = 1
cnt = 0
for i in str:
    if i == 'M':
        cnt += 1
        tmp *= 10
    elif i == 'K':
        flag = 0
        tmp *= 5
        print(tmp, end="")
        tmp = 1

if tmp >= 10:
    if flag:
        while cnt:
            print(1, end="")
            cnt -= 1
    else:
        while tmp // 10:
            print(1, end="")
            tmp /= 10
print()

tmp = 1
for i in str:
    if i == 'M':
        tmp *= 10
    elif i == 'K':
        if tmp >= 10:
            print(tmp//10, end="")
        tmp = 1
        print(5, end="")

if tmp >= 10:
    print(tmp//10, end="")
print()
