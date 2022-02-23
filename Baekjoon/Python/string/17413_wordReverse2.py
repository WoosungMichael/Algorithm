S = input()

tmp =[]
flag = False
for i in range(len(S)):
    if flag:
        if S[i] == ">":
            print(">", end = "")
            flag = False
        else:
            print(S[i], end = "")
    else:
        if S[i] == "<":
            if len(tmp) != 0:
                tmp.reverse()
                for j in tmp:
                    print(j, end = "")
                tmp = []
            print("<", end = "")
            flag = True
        elif S[i] == " ":
            tmp.reverse()
            for j in tmp:
                print(j, end = "")
            print(" ", end = "")
            tmp = []
        elif i == len(S) - 1:
            tmp.append(S[i])
            tmp.reverse()
            for j in tmp:
                print(j, end = "")
            tmp = []
        else:
            tmp.append(S[i])
