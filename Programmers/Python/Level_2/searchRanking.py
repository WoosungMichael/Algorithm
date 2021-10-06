def solution(info, query):
    answer = []
    tmp_i = []
    tmp_q = []
    for i in info:
        tmp_i.append(i.split(" "))

    for i in query:
        tmp_q.append(i.replace("- ", "").replace("and ", "").split(" "))

    for i in tmp_q:
        cnt = 0
        for j in tmp_i:
            flag = True
            for k in range(len(i)-1):
                if i[k] not in j:
                    flag = False
                    break
            if int(i[-1]) > int(j[4]):
                flag = False
            if flag:
                cnt += 1
        answer.append(cnt)
    return answer
