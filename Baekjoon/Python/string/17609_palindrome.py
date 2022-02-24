T = int(input())

for i in range(T):
    word = input()
    l = 0
    r = len(word) - 1
    flag = 0
    flag1 = False
    while (l <= r):
        if word[l] == word[r]:
            l += 1
            r -= 1
        elif flag == 0:
            flag = 1
            if word[l + 1] == word[r]:
                l += 2
                r -= 1
                flag1 = True
            elif word[l] == word[r - 1]:
                l += 1
                r -= 2
            else:
                flag = 2
                break
        elif flag == 1:
            if word[l - 2] == word[r] and flag1:
                l -= 1
                r -= 1
                flag1 = False
            else:
                flag = 2
                break
    print(flag)
