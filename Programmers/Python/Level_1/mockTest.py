def solution(answers):
    answer = []
    
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if a1[i % 5] == answers[i]:
            cnt[0] += 1
        if a2[i % 8] == answers[i]:
            cnt[1] += 1
        if a3[i % 10] == answers[i]:
            cnt[2] += 1
    
    max_cnt = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == max_cnt:
            answer.append(i + 1)
        
    return answer