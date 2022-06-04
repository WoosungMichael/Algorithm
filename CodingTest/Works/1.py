def solution(bakery_schedule, current_time, K):
    answer = -1
    sum = 0
    for element in bakery_schedule:
        a, b = element.split()
        h, m = map(int, a.split(':'))
        c_h, c_m = map(int, current_time.split(':'))
        if h < c_h or (h == c_h and m < c_m):
            continue
        else:
            sum += int(b)
        if sum >= K:
            answer = (h * 60 + m) - (c_h * 60 + c_m)
            break
    return answer