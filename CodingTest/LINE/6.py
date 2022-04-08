def solution(req_id, req_info):
    answer = []
    buy = []
    sell = []
    
    result_amount = {}
    result_price = {}
    for i in req_id:
        result_amount[i] = 0
        result_price[i] = 0

    for i in range(len(req_info)):
        if req_info[i][0] == 0:
            for j in sell:
                if req_info[i][2] >= j[2]:
                    amount = min(req_info[i][1], j[1])
                    req_info[i][1] -= amount
                    j[1] -= amount
                    result_amount[req_id[i]] += amount
                    result_amount[j[0]] -= amount
                    result_price[req_id[i]] -= amount * j[2]
                    result_price[j[0]] += amount * j[2]
                    if req_info[i][1] == 0:
                        break

            if req_info[i][1] > 0:
                req_info[i][0] = req_id[i]
                
                buy.append(req_info[i])
                buy.sort(reverse = True)
            
        else:
            for j in buy:
                if req_info[i][2] <= j[2]:
                    amount = min(req_info[i][1], j[1])
                    req_info[i][1] -= amount
                    j[1] -= amount
                    result_amount[req_id[i]] -= amount
                    result_amount[j[0]] += amount
                    result_price[req_id[i]] += amount * req_info[i][2]
                    result_price[j[0]] -= amount * req_info[i][2]
                    if req_info[i][1] == 0:
                        break

            if req_info[i][1] > 0:
                req_info[i][0] = req_id[i]
                
                sell.append(req_info[i])
                sell.sort()

    result_amount = dict(sorted(result_amount.items()))

    for i in result_amount:
        result = i
        result += " "
        if result_amount[i] > 0:
            result += "+"
        result += str(result_amount[i])
        result += " "
        if result_price[i] > 0:
            result += "+"
        result += str(result_price[i])

        answer.append(result)

    return answer