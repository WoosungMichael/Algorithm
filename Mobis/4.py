import copy


def solution(p, q):
    answer = []
    for i in range(len(p)):
        p[i].sort()
        q[i].sort()

        p_index = 0
        q_index = copy.deepcopy(len(q[i]))

        for j in range(q_index):
            flag = True
            if(p[i][p_index] > q[i][j]):
                answer.append(False)
                flag = False
                break
            elif p[i][p_index] == q[i][j]:
                p_index += 1
            elif p[i][p_index] < q[i][j]:
                if len(p[i]) != p_index:
                    p_index += 1
                    p[i][p_index] += p[i][p_index-1]
                    j -= 1
                else:
                    answer.append(False)
                    flag = False
        if flag:
            answer.append(True)

    return answer


p = [[4, 3, 3], [1, 2, 3], [3, 2, 4]]
q = [[5, 5], [5, 1], [1, 8]]
print(solution(p, q))
