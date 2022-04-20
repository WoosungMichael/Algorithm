def solution(bishops):
    answer = 64
    visited = [([0] * 8) for i in range(8)]
    for i in bishops:
        x = ord(i[0]) - ord('A')
        y = int(i[1]) - 1
        for j in range(-8, 8):
            if x + j >= 0 and x + j < 8 and y + j >= 0 and y + j < 8 and visited[x + j][y + j] == 0:
                visited[x + j][y + j] = 1
                answer -= 1
            if x + j >= 0 and x + j < 8 and y - j >= 0 and y - j < 8 and visited[x + j][y - j] == 0:
                visited[x + j][y - j] = 1
                answer -= 1

    return answer


# 비숍 위치 주어지고 비숍이 갈 수 없는 칸 수 구하기