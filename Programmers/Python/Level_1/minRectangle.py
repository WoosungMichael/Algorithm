def solution(sizes):
    tmp1 = 0
    tmp2 = 0
    for i in sizes:
        if i[0] > i[1]:
            if tmp1 < i[0]:
                tmp1 = i[0]
            if tmp2 < i[1]:
                tmp2 = i[1]
        else:
            if tmp1 < i[1]:
                tmp1 = i[1]
            if tmp2 < i[0]:
                tmp2 = i[0]
    answer = tmp1 * tmp2
    return answer
