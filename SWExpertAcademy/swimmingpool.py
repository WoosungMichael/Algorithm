T = int(input())

for _ in range(T):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    for i in range(12):
        if plan[i] * cost[0] > cost[1]:
            plan[i] = cost[1]
        else:
            plan[i] *= cost[0]

    month3 = [[2, 5, 8, 11], [3, 6, 9], [3, 6, 10], [3, 6, 11], [3, 7, 10], [3, 7, 11],
              [3, 8, 11], [4, 7, 10], [4, 7, 11], [4, 8, 11]]
    global_min = cost[3]
    for i in month3:
        tmp = 0
        index = 0
        for j in i:
            while index < j - 2:
                tmp += plan[index]
                index += 1
            index = j + 1
            if plan[j - 2] + plan[j - 1] + plan[j] > cost[2]:
                tmp += cost[2]
            else:
                tmp += plan[j - 2] + plan[j - 1] + plan[j]
        while index < 12:
            tmp += plan[index]
            index += 1
        if tmp < global_min:
            global_min = tmp

    print("#" + str(_ + 1) + " " + str(global_min))