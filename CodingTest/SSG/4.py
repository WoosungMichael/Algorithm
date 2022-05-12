import copy

def solution(casted):
    answer = 0
    point = [0] * 13
    q=[point]
    for c in range(len(casted)):
        point_sum = sum(casted[c])
        tmp = []
        for arr in q:
            tmp.append(arr)
            for j in range(0, point_sum // 2 + 1):
                tmp_arr = copy.deepcopy(arr)
                if tmp_arr[j] == 0:
                    if j != 0:
                        tmp_arr[j] = 1
                else:
                    continue
                if tmp_arr[point_sum - j] == 0:
                    tmp_arr[point_sum - j] = 1
                else:
                    continue
                if sum(tmp_arr) == 12:
                    return c + 1
                tmp.append(tmp_arr)
            
        tmp = list(set(map(tuple, tmp)))
        q = []
        for t in tmp:
            q.append(list(t))
    return answer
