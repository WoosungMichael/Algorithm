def solution(brown, yellow): 
    y = 3
    while (True):
        x = brown / 2 + 2 - y
        if (x - 2) * (brown / 2 - x) == yellow:
            answer = [x, y]
            break
        y += 1
    return answer