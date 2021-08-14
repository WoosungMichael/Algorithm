def solution(seoul):
    answer = "김서방은 "
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer += str(i)
    answer += "에 있다"
    return answer
