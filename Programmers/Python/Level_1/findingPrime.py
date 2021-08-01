def solution(n):
    answer = 0

    if(n > 1):
        answer = 1

    for i in range(3, n+1):
        if(i % 2 == 0):
            continue
        else:
            cnt = 0
            flag = True
            for j in range(2, int(i**0.5)+1):
                if(i % j == 0):
                    cnt += 1
                    flag = False
                    break
            if(flag):
                answer += 1

    return answer
