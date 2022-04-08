def solution(abilities, k):
    answer = 0
    abilities.sort(reverse = True)

    gap = []
    for i in range(0, len(abilities), 2):
        if i + 1 == len(abilities):
            gap.append(abilities[i])
        else:
            gap.append(abilities[i] - abilities[i + 1])

    for i in range(len(abilities)):
        if i % 2 == 1:
            answer += abilities[i]
    
    gap.sort(reverse = True)
    for i in range(k):
        answer += gap[i]

    return answer