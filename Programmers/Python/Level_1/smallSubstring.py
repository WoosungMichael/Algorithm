def solution(t, p):
    answer = 0
    l1 = len(t)
    l2 = len(p)
    for i in range(l1 - l2 + 1):
        if(int(t[i:i + l2]) <= int(p)):
            answer += 1
    return answer
