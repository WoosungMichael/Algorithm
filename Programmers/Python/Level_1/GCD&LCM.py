def solution(n, m):
    answer = []
    min_n = min(n, m)
    max_n = max(n, m)

    for i in range(min_n, 0, -1):
        if(max_n % i == 0 and min_n % i == 0):
            answer.append(i)
            break

    for i in range(max_n, max_n*min_n+1):
        if(i % max_n == 0 and i % min_n == 0):
            answer.append(i)
            break

    return answer
