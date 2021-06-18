def solution(a, b):
    answer = 0
    for index in range(len(a)):
        answer += a[index] * b[index]
    return answer