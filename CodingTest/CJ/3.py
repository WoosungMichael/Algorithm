def solution(wolf_count, sheep_count, cabbage_count, wolf_weight, sheep_weight, cabbage_weight, limit):
    answer = 0
    if wolf_count * wolf_weight + sheep_count * sheep_weight + cabbage_count * cabbage_weight <= limit:
        return 1
    if wolf_count == sheep_count and sheep_count == cabbage_count and wolf_count * wolf_weight == limit and sheep_count * sheep_weight == limit and cabbage_count * cabbage_weight == limit:
        return 7

    while True:
        if wolf_count == 0 and sheep_count == 0 and cabbage_count == 0:
            break
        if answer > wolf_count + sheep_count + cabbage_count:
            break
        answer += 1
        tmp = 0
        if wolf_count >= sheep_count:
            if tmp + sheep_count * sheep_weight <= limit:
                tmp += sheep_count * sheep_weight
                sheep_count = 0
            elif tmp + (wolf_count - sheep_count + 1) * wolf_weight <= limit:
                tmp += (limit - tmp) // wolf_weight * wolf_count
                wolf_count -= (limit - tmp) // wolf_weight
            else:
                return -1

        if sheep_count >= cabbage_count:
            if tmp + cabbage_count * cabbage_weight <= limit:
                tmp += cabbage_count * cabbage_weight
                cabbage_count = 0
            elif tmp + (sheep_count - cabbage_count + 1) * sheep_weight <= limit:
                tmp += (limit - tmp) // sheep_weight * sheep_count
                sheep_count -= (limit - tmp) // sheep_weight
            else:
                return -1

    if answer == 0:
        return -1
    return answer