def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    arr = []
    for i in range(row_begin - 1, row_end):
        tmp = 0
        for j in range(len(data[0])):
            tmp += data[i][j] % (i + 1)
        arr.append(tmp)
    for i in arr:
        answer ^= i
    return answer
