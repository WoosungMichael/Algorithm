str = input()

while (str != "*"):
    flag = True
    for i in range(1, len(str)):
        tmp = []
        tmp_s = ""
        index = 0

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
