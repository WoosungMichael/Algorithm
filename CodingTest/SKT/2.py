from collections import deque

def solution(total_sp, skills):
    answer = [0] * (len(skills) + 1)
    arr = []

    for i in range(len(skills) + 2):
        arr.append("")
    for i in skills:
        arr[i[0]] += str(i[1])
    for i in range(1, len(arr)):
        if arr[i] == '':
            arr[i] = 'a'

    q = deque()
    b = []
    a = []
    for i in skills:
        a.append(i[0])
        b.append(i[1])

    a = list(set(a))
    b = list(set(b))
    start = 0
    for i in a:
        if i not in b:
            start = i
            break

    q.append(start)
    flag = True

    visited = [0] * (len(skills) + 2)
    total = []
    while q:
        tmp = int(q.popleft())

        for i in arr[tmp]:
            if i != 'a':
                q.append(i)
                if visited[int(i)] != 1:
                    q.append(i)
                visited[int(i)] = 1
            else:
                total.append(i)

    base = total_sp // len(total)

    node = deque()
    for i in b:
        if i not in a:
            answer[i - 1] = base
            node.append(i)

    visited = [0] * (len(skills) + 2)
    while node:
        i = node.popleft()
        for j in skills:
            if i == j[1]:
                if visited[i] == 0:
                    answer[j[0] - 1] += answer[i - 1]
                    node.append(j[0])
                    visited[i] = 1
    return answer


# 스킬 트리 주어지고 각 스킬 점수 배열로 반환하기
# 상위 스킬 점수는 선행 스킬들 점수 합
# 가장 하위 스킬 점수는 모두 동일
# 총 스킬 점수 합 : total_sp