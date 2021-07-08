def solution(files):
    answer = []
    arr = []
    for i in files:
        str1 = ""
        str2 = ""
        flag = False
        index = 0
        for j in range(len(i)):
            if(i[j] < "0" or i[j] > "9"):
                if(flag):
                    index = j
                    break
                str1 += i[j]

            else:
                str2 += i[j]
                flag = True
        str3 = i[index:]
        if(str3 == i):
            str3 = ""
        arr.append([str1, str2, str3])
    arr.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for i in arr:
        str = i[0]+i[1]+i[2]
        answer.append(str)

    return answer
