from itertools import combinations
import math

def solution(fuel, powers, distances):
    cnt = len(powers)
    tmp = []
    for i in range(fuel - 1):
        tmp.append(i)
    f_list = list(combinations(tmp, cnt - 1))

    answer = float('inf')
    for i in f_list:
        index = -1
        tmp = 0
        for j in range(len(i)):
            if tmp < ((i[j] - index) / 2) + (distances[j] / (powers[j] * (i[j] - index))):
                tmp = ((i[j] - index) / 2) + (distances[j] / (powers[j] * (i[j] - index)))
            index = i[j]
        if tmp < ((fuel - index - 1) / 2) + (distances[-1] / (powers[-1] * (fuel - index - 1))):
            tmp = ((fuel - index - 1) / 2) + (distances[-1] / (powers[-1] * (fuel - index - 1)))
        if answer > tmp:
            answer = tmp

    return math.ceil(answer)