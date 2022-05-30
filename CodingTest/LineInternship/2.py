def solution(n, times):
    answer = 0
    times_new = [times[0], min(times[0] * 2, times[1])]

    for i in range(2, len(times)):
        times_new.append(min(times_new[i - 1] + times_new[0], times[i]))

    cnt = 1
    while True:
        if cnt == n:
            break

        if cnt * 2 <= n:
            answer += times_new[cnt - 1]
            cnt *= 2
        else:
            answer += times_new[n - cnt - 1]
            cnt += n - cnt

    return answer