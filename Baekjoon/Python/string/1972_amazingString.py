str = input()

while (str != "*"):
    for i in range(1, len(str)-1):
        tmp = []
        tmp_s = ""
        index = 0
        flag = True
        while index + i < len(str):
            tmp_s = str[index] + str[index + i]
            tmp.append(tmp_s)
            index += 1
        if (len(tmp) != len(list(set(tmp)))):
            flag = False
            break
    if flag:
        print(str, end="")
        print(" is surprising.")
    else:
        print(str, end="")
        print(" is NOT surprising.")

    str = input()
