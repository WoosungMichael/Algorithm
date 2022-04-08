def solution(num_teams, remote_tasks, office_tasks, employees):
    office_worker = []
    team = [[] for i in range(num_teams + 1)]
    for i in range(len(employees)):
        team[int(employees[i].split()[0])].append(i + 1)

    for i in team:
        if i == []:
            continue
        flag = True
        for j in i:
            work_list = employees[j - 1].split()[1:]
            for k in work_list:
                if k in office_tasks:
                    flag = False
                    office_worker.append(j)
        if flag:
            office_worker.append(i[0])

    office_worker = list(set(office_worker))
    office_worker.sort()

    workers = [(i + 1) for i in range(len(employees))]
    answer = [i for i in workers if i not in office_worker]

    return answer