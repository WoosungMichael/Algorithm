def solution(goods):
    answer = []
    for i in range(len(goods)):
        key_f = True
        for cnt in range(1, len(goods[i]) + 1):
            tmp = []
            for j in range(len(goods[i]) - cnt + 1):
                flag = True
                str = goods[i][j:j + cnt]
                for k in range(len(goods)):
                    if i != k:
                        if goods[k].find(str) != -1:
                            flag = False
                if flag:
                    tmp.append(str)
            if len(tmp) != 0:
                tmp = list(set(tmp))
                tmp.sort()
                keyword = " ".join(tmp)
                answer.append(keyword)
                key_f = False
                break
        if key_f:
            answer.append("None")
       
    return answer
