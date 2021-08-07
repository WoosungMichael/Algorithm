def solution(s):
    answer = ''
    arr_l = []
    arr_u = []
    for i in s:
        if(i.islower()):
            arr_l.append(i)
        else:
            arr_u.append(i)
    arr_l.sort(reverse=True)
    arr_u.sort(reverse=True)
    answer += ''.join(arr_l)
    answer += ''.join(arr_u)
    return answer
