import copy


def solution(n, t, m, p):
    answer = ''
    cnt = 0
    flag = False

    number = 0
    while(True):
        tmp = ""
        if(flag):
            break
        num = copy.deepcopy(number)
        while(num >= n):
            if(num % n < 10):
                tmp += str(num % n)
                cnt += 1
            elif(num % n == 10):
                tmp += 'A'
                cnt += 1
            elif(num % n == 11):
                tmp += 'B'
                cnt += 1
            elif(num % n == 12):
                tmp += 'C'
                cnt += 1
            elif(num % n == 13):
                tmp += 'D'
                cnt += 1
            elif(num % n == 14):
                tmp += 'E'
                cnt += 1
            elif(num % n == 15):
                tmp += 'F'
                cnt += 1
            num = num//n
            if(cnt == n*t):
                flag = True
        if(num < 10):
            tmp += str(num % n)
            cnt += 1
        elif(num == 10):
            tmp += 'A'
            cnt += 1
        elif(num == 11):
            tmp += 'B'
            cnt += 1
        elif(num == 12):
            tmp += 'C'
            cnt += 1
        elif(num == 13):
            tmp += 'D'
            cnt += 1
        elif(num == 14):
            tmp += 'E'
            cnt += 1
        elif(num == 15):
            tmp += 'F'
            cnt += 1

        tmp_list = list(tmp)
        tmp_list.reverse()
        tmpR = ''.join(tmp_list)
        answer += tmpR
        if(cnt == n*t):
            flag = True
        number += 1

    result = ""

    for i in range(len(answer)):
        if(i % m == (p-1)):
            result += answer[i]
        if(len(result) == t):
            break

    return result
