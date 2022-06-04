def solution(n):
    num = [(i + 1) for i in range(n)]
    answer = mix(num)
    return answer

def mix(num):
    length = len(num)
    if length == 1:
        return num
    p = 2
    for i in range(2, length + 1):
        if length % i == 0:
            p = i
            break
    tmp = [[]for _ in range(p)]
    index = 0
    for i in range(length):
        tmp[i % p].append(num[i])
    arr = []
    for i in range(p):
        arr += mix(tmp[i])
    return arr