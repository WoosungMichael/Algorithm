def solution(id_list, report, k):
    cntlist = [0 for i in range(len(id_list))]
    idlist = [[] for i in range(len(id_list))]
    dict = {}
    for i in range(len(id_list)):
        dict[id_list[i]] = i
    for i in report:
        x, y = i.split()
        if x not in idlist[dict[y]]:
            cntlist[dict[y]] += 1
            idlist[dict[y]].append(x)
    
    answer = [0 for i in range(len(id_list))]
    
    for i in range(len(cntlist)):
        if cntlist[i] >= int(k):
            for j in idlist[i]:
                answer[dict[j]] += 1
    return answer