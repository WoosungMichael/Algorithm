def solution(word):
    answer = 0
    for i in range(len(word)):
        if word[i] == 'A':
            tmp = 0
        elif word[i] == 'E':
            tmp = 1
        elif word[i] == 'I':
            tmp = 2
        elif word[i] == 'O':
            tmp = 3
        elif word[i] == 'U':
            tmp = 4
        tmp2 = 0
        for j in range(1, 5-i):
            tmp2 += 5 ** j
        answer += tmp * tmp2
        answer += 1
        answer += tmp
    return answer
