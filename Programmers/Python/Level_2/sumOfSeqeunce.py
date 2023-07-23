def solution(sequence, k):
    answer = []
    length = len(sequence)
    
    if sequence[0] == k:
        return [0,0]
    
    p_sum = 0
    l, r = 0, 0
    while l <= r and r < len(sequence):
        while r < len(sequence):
            if p_sum + sequence[r] < k:
                p_sum += sequence[r]
                r += 1
            elif p_sum + sequence[r] == k:
                p_sum = k
                if length > r - l:
                    answer = [l, r]
                    length = r - l
                r += 1
                break
            else:
                break
        p_sum -= sequence[l]
        l += 1
        if l > r:
            r = l
    
    return answer
