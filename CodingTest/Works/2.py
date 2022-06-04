def solution(N, K, charges):
    answer = []
    station = [0 for _ in range(N)]
    time = 0
    index = 0
    while True:
        for i in range(len(station)):
            if station[i] <= time:
                if index == K - 1:
                    answer = [i + 1, time + charges[index]]
                    return answer
                station[i] += charges[index]
                index += 1
        time += 1
    return answer