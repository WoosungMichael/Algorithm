def solution(money, costs):
    answer = 0
    coin = [1, 5, 10, 50, 100, 500]
    flag = [True for i in range(6)]
    tmp = [costs[0] * 500, costs[1] * 100, costs[2] * 50, costs[3] * 10, costs[4] * 5, costs[5]]
    min = tmp[0]
    for i in range(1, len(tmp)):
        if tmp[i] > min:
            flag[i] = False
        else:
            min = tmp[i]
    
    for i in reversed(range(len(coin))):
        if flag[i] and money >= coin[i]:
            answer += (money // coin[i]) * costs[i]
            money -= (money // coin[i]) * coin[i]
    return answer