import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        if i <= r1:
            tmp = math.sqrt((r1 ** 2) - (i ** 2))
            if tmp == int(tmp):
                y1 = int(tmp)
            else:
                y1 = int(tmp) + 1
        else:
            y1 = 0
        y2 = int(math.sqrt((r2 ** 2) - (i ** 2)))
        
        answer += (y2 - y1 + 1)
    
    answer *= 4
            
    return answer
