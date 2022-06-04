from itertools import combinations_with_replacement
from collections import deque

def solution(N, money, T, K):
    answer = 0
    tmp = [i for i in range(money + 1)]
    arr = list(combinations_with_replacement(tmp, N - 1))

    for i in arr:
        last = 0
        q = deque()
        q_sum = 0
        flag = False
        for j in i:
            if len(q) == T:
                q_sum -= q.popleft()
            q_sum += j - last
            q.append(j - last)
            if q_sum > K:
                flag = True
                break
            last = j
        if len(q) == T:
            q_sum -= q.popleft()
        q_sum += money - last
        if q_sum > K:
            flag = True
        if flag:
            continue
        answer += 1

    return answer