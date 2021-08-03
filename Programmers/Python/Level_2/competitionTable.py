import math


def solution(n, a, b):
    answer = 0

    minN = min(a, b)
    maxN = max(a, b)

    left = 0
    right = n
    mid = n//2
    while(True):
        if minN <= mid and maxN > mid:
            answer += 1
            break
        elif minN > mid:
            mid = (mid+right)//2
            left = mid
            answer += 1
        elif maxN <= mid:
            mid = (left+mid)//2
            right = mid
            answer += 1

    answer = math.log2(n)+1-answer
    return answer
