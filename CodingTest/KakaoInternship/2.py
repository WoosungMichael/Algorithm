from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum1, sum2 = 0, 0
    q1, q2 = deque(), deque()
    len1, len2 = len(queue1), len(queue2)
    for i in queue1:
        sum1 += i
        q1.append(i)
    for i in queue2:
        sum2 += i
        q2.append(i)

    if sum1 == sum2:
        return 0
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    while answer < len1 + len2:
        if sum1 < sum2:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        elif sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum2 += tmp
            sum1 -= tmp
        else:
            return answer
        answer += 1
    return -1