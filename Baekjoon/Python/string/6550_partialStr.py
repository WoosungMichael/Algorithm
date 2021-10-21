while 1:
    s, t = input().split()

    flag1 = True
    index = -1
    for i in s:
        flag = True
        for j in range(index+1, len(t)):
            if index + 1 < len(t) and i == t[j]:
                index = j
                flag = False
                break
        if flag:
            print("No")
            flag1 = False
            break
    if flag1:
        print("Yes")
