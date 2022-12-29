def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = sorted(dic.items(), key=lambda x: -x[1])
    for i in dic:
        answer += 1
        if k - i[1] <= 0:
            break
        else:
            k -= i[1]
    return answer
