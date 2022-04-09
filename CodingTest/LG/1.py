def solution(user_times, T):
    arr = []
    for i in user_times:
        if i % T == 0:
            arr.append(0)
        else:
            arr.append(T - (i % T))
    answer = max(arr)
    return answer