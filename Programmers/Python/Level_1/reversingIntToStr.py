def solution(n):
    answer = []
    n_str = str(n)
    tmp = n_str[::-1]
    for i in tmp:
        answer.append(int(i))
    return answer
