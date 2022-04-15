def solution(h, w, blocks):
    answer = [w for i in range(h)]
    visited = [([0] * w) for i in range(h)]
    for i in blocks:
        y, x = i
        if visited[h - x - 1][y] == 0:
            visited[h - x - 1][y] = 1
            answer[h - x - 1] -= 1

    for i in range(h - 2, -1, -1):
        answer[i] += answer[i + 1]
    answer.reverse()
    return answer