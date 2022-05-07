def solution(survey, choices):
    answer = ''
    score = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for s in range(len(survey)):
        if choices[s] > 4:
            score[survey[s][1]] += choices[s] - 4
        elif choices[s] < 4:
            score[survey[s][0]] += 4 - choices[s]

    if score['R'] < score['T']:
        answer += "T"
    else:
        answer += "R"
    if score['C'] < score['F']:
        answer += "F"
    else:
        answer += "C"
    if score['J'] < score['M']:
        answer += "M"
    else:
        answer += "J"
    if score['A'] < score['N']:
        answer += "N"
    else:
        answer += "A"

    return answer