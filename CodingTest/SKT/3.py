from collections import deque

def solution(topping, tasting):
    q = deque()
    taste = [tasting[0]]
    for i in range(1, len(tasting)):
        if tasting[i] != tasting[i - 1]:
            taste.append(tasting[i])

    answer = len(topping) * 4
    q.append([0, 0, 0])
    while q:
        tmp = q.popleft()
        if tmp[2] >= answer:
            continue
        if tmp[1] == len(tasting):
            if tmp[2] < answer:
                answer = tmp[2]
                continue

        index_r = tmp[0]
        cnt_r = 0
        while topping[index_r % len(topping)] != tasting[tmp[1]]:
            index_r += 1
            cnt_r += 1
        q.append([index_r % len(topping), tmp[1] + 1, tmp[2] + cnt_r])

        index_l = tmp[0]
        cnt_l = 0
        while topping[index_l % len(topping)] != tasting[tmp[1]]:
            index_l -= 1
            cnt_l += 1
        q.append([index_l % len(topping), tmp[1] + 1, tmp[2] + cnt_l])

    return answer


# 피자 토핑 주어지고 먹으려는 토핑 주어짐
# 최소로 칸 이동하며 다 먹을 수 있는 방법