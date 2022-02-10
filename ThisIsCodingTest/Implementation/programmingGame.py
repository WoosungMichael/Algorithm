def nextStep(gameMap, mapFlag, r, c, d, cnt):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    if gameMap[r + dx[d]][c + dy[d]] == 0 and mapFlag[r + dx[d]][c + dy[d]] == 0:
        cnt += 1
        mapFlag[r + dx[d]][c + dy[d]] = 1
        return(nextStep(gameMap, mapFlag, r + dx[d], c + dy[d], d, cnt))
    elif gameMap[r + dx[(d + 3) % 4]][c + dy[(d + 3) % 4]] == 0 and mapFlag[r + dx[(d + 3) % 4]][c + dy[(d + 3) % 4]] == 0:
        cnt += 1
        mapFlag[r + dx[(d + 3) % 4]][c + dy[(d + 3) % 4]] = 1
        return(nextStep(gameMap, mapFlag, r + dx[(d + 3) % 4], c + dy[(d + 3) % 4], (d + 3) % 4, cnt))
    elif gameMap[r + dx[(d + 2) % 4]][c + dy[(d + 2) % 4]] == 0 and mapFlag[r + dx[(d + 2) % 4]][c + dy[(d + 2) % 4]] == 0:
        cnt += 1
        mapFlag[r + dx[(d + 2) % 4]][c + dy[(d + 2) % 4]] = 1
        return(nextStep(gameMap, mapFlag, r + dx[(d + 2) % 4], c + dy[(d + 2) % 4], (d + 2) % 4, cnt))
    elif gameMap[r + dx[(d + 1) % 4]][c + dy[(d + 1) % 4]] == 0 and mapFlag[r + dx[(d + 1) % 4]][c + dy[(d + 1) % 4]] == 0:
        cnt += 1
        mapFlag[r + dx[(d + 1) % 4]][c + dy[(d + 1) % 4]] = 1
        return(nextStep(gameMap, mapFlag, r + dx[(d + 1) % 4], c + dy[(d + 1) % 4], (d + 1) % 4, cnt))
    elif gameMap[r - dx[d]][c - dy[d]] == 0:
        return(nextStep(gameMap, mapFlag, r - dx[d], c - dy[d], d, cnt))
    else:
        return cnt


N, M = map(int, input().split())
r, c, d = map(int, input().split())

gameMap = []
for i in range(N):
    gameMap.append(list(map(int, input().split())))

mapFlag = [[0 for i in range(M)]for j in range(N)]
mapFlag[r][c] = 1
cnt = 1

print(nextStep(gameMap, mapFlag, r, c, d, cnt))