def solution(replies, n, k):
    answer = []
    for re in replies:
        pattern = {}
        flag2 = False
        for i in range(len(re) - n + 1):
            str = ""
            for j in range(i, i + n):
                str += re[j]
            if str in pattern:
                i1 = pattern[str] + n
                i2 = i + n
                flag = True
                while i1 < i:
                    if i2 < len(re) and re[i1] == re[i2]:
                        i1 += 1
                        i2 += 1
                    else:
                        flag = False
                        break
                if flag:
                    tmp = k - 2
                    start = i2
                    s_i = i
                    while tmp:
                        for _ in range(i - pattern[str]):
                            if start < len(re) and re[start] == re[s_i]:
                                start += 1
                                s_i += 1
                            else:
                                flag = False
                                break
                        if flag == False:
                            break
                        tmp -= 1
                    if flag:
                        flag2 = True
                        break
                pattern[str] = i
            else:
                pattern[str] = i

        if flag2:
            answer.append(0)
        else:
            answer.append(1)

    return answer