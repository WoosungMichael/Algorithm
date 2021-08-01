def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)]

    i = 0
    while(i < len(truck_weights)):
        bridge.pop(0)
        if(sum(bridge)+truck_weights[i] <= weight):
            print(sum(bridge)+truck_weights[i])
            bridge.append(truck_weights[i])
        else:
            bridge.append(0)
            i -= 1

        i += 1
        answer += 1

    return answer + bridge_length
