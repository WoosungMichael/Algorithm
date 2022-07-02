def solution(n, recent, recently_use, total_use, records):
    answer = []
    app = []
    for i in range(n):
        app.append([i, 0, 0])
    for rec in records:
        if rec[0] <= recent:
            app[rec[1] - 1][1] += rec[2]
        app[rec[1] - 1][2] += rec[2]
    for i in app:
        if i[1] <= recently_use and i[2] < total_use:
            answer.append(i[0] + 1)
    return answer