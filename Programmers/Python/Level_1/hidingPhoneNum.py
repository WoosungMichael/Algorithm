def solution(phone_number):
    answer = ''
    numLen = len(phone_number)
    for i in range(numLen):
        if i < numLen - 4:
            answer += "*"
        else:
            answer += phone_number[i]
    return answer
