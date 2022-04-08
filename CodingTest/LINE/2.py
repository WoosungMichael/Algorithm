from itertools import combinations

def solution(sentences, n):
    answer = -1
    alpha = []
    
    #shift O
    for i in sentences:
        for j in i:
            if j != " ":
                if ord('A') <= ord(j) and ord(j) <= ord('Z'):
                    alpha.append(chr(ord(j) + 32))
                else:
                    alpha.append(j)
        alpha = list(set(alpha))

    combo = list(combinations(alpha, n - 1))
    
    max_cnt1 = 0
    for i in combo:
        cnt = 0
        for j in sentences:
            tmp_cnt = 0
            flag = True
            for k in j:
                if k != " ":
                    if k not in i and chr(ord(k) + 32) not in i:
                        flag = False
                        break
                if ord('A') <= ord(k) and ord(k) <= ord('Z'):
                    tmp_cnt += 1
            if flag:
                tmp_cnt += len(j)
            else:
                tmp_cnt = 0
            cnt += tmp_cnt
        if cnt > max_cnt1:
            max_cnt1 = cnt


    for i in sentences:
        for j in i:
            if ord('a') <= ord(j) and ord(j) <= ord('z'):
                alpha.append(j)
        alpha = list(set(alpha))

    combo = list(combinations(alpha, n))

    max_cnt2 = 0
    for i in combo:
        cnt = 0
        for j in sentences:
            tmp_cnt = 0
            flag = True
            for k in j:
                if k != " " and k not in i:
                    flag = False
                    break
            if flag:
                tmp_cnt += len(j)
            else:
                tmp_cnt = 0
            cnt += tmp_cnt
        if cnt > max_cnt2:
            max_cnt2 = cnt

    answer = max(max_cnt1, max_cnt2)
    
    return answer