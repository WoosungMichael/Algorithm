def solution(n):
    answer = 0
    for i in range(1, n + 1):
        tmp = 0
        j = i
        while tmp <= n:
            tmp += j
            j += 1
            if tmp == n:
                answer += 1
            elif tmp > n:
                break
    return answer