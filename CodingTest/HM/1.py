def solution(n, k, floors):
    answer = []
    empty = [k] * n
    for i in floors:
        if empty[i - 1] > 0:
            answer.append(i)
            empty[i - 1] -= 1
        else:
            tmp = 1
            while True:
                if i - tmp - 1 >= 0 and empty[i - tmp - 1] > 0:
                    answer.append(i - tmp)
                    empty[i - tmp - 1] -= 1
                    break
                elif i + tmp - 1 < n and empty[i + tmp - 1] > 0:
                    answer.append(i + tmp)
                    empty[i + tmp - 1] -= 1
                    break
                tmp += 1
    return answer