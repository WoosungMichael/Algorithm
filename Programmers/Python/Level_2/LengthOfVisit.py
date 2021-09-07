def solution(dirs):
    answer = 0
    arr = []
    now = [0, 0]
    for i in dirs:
        tmp = []
        if(i == 'U' and now[1] != 5):
            now[1] += 1
            tmp = [now[0], now[1], 1]
            if tmp not in arr:
                answer += 1
                arr.append(list(tmp))
        elif(i == 'D' and now[1] != -5):
            now[1] -= 1
            tmp = [now[0], now[1]+1, 1]
            if tmp not in arr:
                answer += 1
                arr.append(list(tmp))
        elif(i == 'L' and now[0] != -5):
            now[0] -= 1
            tmp = [now[0]+1, now[1], 0]
            if tmp not in arr:
                answer += 1
                arr.append(list(tmp))
        elif(i == 'R' and now[0] != 5):
            now[0] += 1
            tmp = [now[0], now[1], 0]
            if tmp not in arr:
                answer += 1
                arr.append(list(tmp))

    return answer
