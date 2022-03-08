from itertools import permutations 
import copy

def solution(k, dungeons):
    cnt = 0
    tmp = copy.deepcopy(k)
    d_list = list(permutations(dungeons, len(dungeons)))
    for i in d_list:
        k = tmp 
        cnt_tmp = 0
        for j in i:
            if k >= j[0]:
                k -= j[1]
                cnt_tmp += 1
        if cnt_tmp > cnt:
            cnt = cnt_tmp
    return cnt