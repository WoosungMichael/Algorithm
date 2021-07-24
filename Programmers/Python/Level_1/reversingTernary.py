import math


def solution(n):
    answer = 0
    str3 = ""
    while(n >= 3):
        str3 += str(n % 3)
        n = n//3
    str3 += str(n)
    str3 = str3[::-1]

    index = 0
    for i in str3:
        answer += int(i)*math.pow(3, index)
        index += 1

    return answer
