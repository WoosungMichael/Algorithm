import itertools


def solution(n, times):
    result = list(itertools.combinations_with_replacement(times, n))
    print(result)
    answer = n*max(times)
    for i in result:
        tmp = 0
        for j in times:
            if(tmp < j*i.count(j)):
                tmp = j*i.count(j)
        if(tmp < answer):
            answer = tmp

    return answer
