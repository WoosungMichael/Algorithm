def solution(a):
    answer = []
    for i in range(len(a)):
        if a[i].count('b') % 2 == 1:
            answer.append(False)
            continue
        while(True):
            tmp_a = a[i].count('a')
            if a[i][0] == 'b' and a[i][-1] == 'b':
                if tmp_a != 0 and a[i][0:tmp_a] == 'b'*tmp_a and a[i][-(tmp_a):] == 'b'*tmp_a:
                    a[i] = a[i][tmp_a:-(tmp_a)]
                else:
                    answer.append(False)
                    break
            a[i] = a[i].strip('a')
            if a[i] == "":
                answer.append(True)
                break

    return answer


a = ["abab", "bbaa", "bababa", "bbbabababbbaa"]

print(solution(a))

'''

        if 0 < a[i].count('b') and a[i].count('b') < a[i].count('a'):
            answer.append(False)
            continue
'''
