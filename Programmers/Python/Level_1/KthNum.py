def solution(array, commands):
    answer = []
    for i in commands:
        tmp = []
        for k in range(i[0] - 1, i[1]):
            tmp.append(array[k])
        tmp.sort()
        answer.append(tmp[i[2] - 1])
    return answer