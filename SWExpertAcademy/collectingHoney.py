from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, M, C = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    profit = []
    for i in range(N):
        for j in range(N - M + 1):
            tmp = []
            for k in range(M):
                tmp_k = list(combinations(arr[i][j:j + M], k + 1))
                tmp_arr = []
                for x in tmp_k:
                    if sum(x) <= C:
                        tmp1 = 0
                        for y in x:
                            tmp1 += y ** 2
                        tmp_arr.append(tmp1)
                if len(tmp_arr) != 0:
                    tmp.append(max(tmp_arr))
            tmp_square = max(tmp)
            if tmp_square != 0:
                profit.append([tmp_square, i, j, j + M - 1])

    profit.sort(key = lambda x : (-x[0]))
    answer1, answer2 = 0, 0
    for i in range(1, len(profit)):
        if profit[i][1] != profit[0][1] or (profit[0][3] < profit[i][2] and 0 <= profit[0][3] - M + 1 and profit[i][2] + M - 1 < N) or (profit[i][3] < profit[0][2] and 0 <= profit[i][3] - M + 1 and profit[0][2] + M - 1 < N):
            answer1 = profit[0][0] + profit[i][0]
            break
    for i in range(2, len(profit)):
        if profit[i][1] != profit[1][1] or (profit[1][3] < profit[i][2] and 0 <= profit[1][3] - M + 1 and profit[i][2] + M - 1 < N) or (profit[i][3] < profit[1][2] and 0 <= profit[i][3] - M + 1 and profit[1][2] + M - 1 < N):
            answer2 = profit[1][0] + profit[i][0]
            break

    print("#" + str(test_case) + " " + str(max(answer1, answer2)))

    # ///////////////////////////////////////////////////////////////////////////////////