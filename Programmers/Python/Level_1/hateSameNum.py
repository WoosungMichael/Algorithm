def solution(arr):
    answer = []
    tmp = -1
    for i in arr:
        if(i != tmp):
            answer.append(i)
        tmp = i
    return answer
