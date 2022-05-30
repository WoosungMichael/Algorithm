def solution(logs):
    answer = []
    prob_d = {}

    logs = list(set(logs))
    for i in logs:
        a, b = map(str, i.split())
        if b in prob_d:
            prob_d[b].append(a)
        else:
            prob_d[b] = [a] 

    people_cnt = len(prob_d)
    for i in prob_d:
        if len(prob_d[i]) >= people_cnt / 2:
            answer.append(i)
    answer.sort()

    return answer