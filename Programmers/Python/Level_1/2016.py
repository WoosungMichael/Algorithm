def solution(a, b):
    answer = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    cnt = 0

    day30 = [4, 6, 9, 11]
    day31 = [1, 3, 5, 7, 8, 10, 12]

    while(a > 1):
        a -= 1
        if(a in day30):
            cnt += 30
        elif(a in day31):
            cnt += 31
        else:
            cnt += 29
    cnt += b
    cnt = cnt % 7

    return answer[cnt]
