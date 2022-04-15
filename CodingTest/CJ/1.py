def solution(room):
    answer = 0
    row = len(room)
    col = len(room[0])
    for i in range(row):
        for j in range(col):
            if room[i][j] == '$':
                tmp = i
                for k in range(i + 1, row):
                    if room[k][j] == '#':
                        break
                    else:
                        tmp = k
                room[tmp] = room[tmp][:j] + '$' + room[tmp][j + 1 :]
                answer += 1
    return answer