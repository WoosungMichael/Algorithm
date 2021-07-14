def solution(lottos, win_nums):
    answer = []
    z_cnt = lottos.count(0)
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1

    rank1 = 7-(cnt+z_cnt)
    rank2 = 7-cnt

    if rank1 == 7:
        rank1 = 6
    if rank2 == 7:
        rank2 = 6

    answer.append(rank1)
    answer.append(rank2)

    return answer
