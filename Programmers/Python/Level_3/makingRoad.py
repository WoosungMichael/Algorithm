from collections import deque

def solution(board):
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    d = 0 # 우하상좌
    
    q = deque()
    arr = [[0] * len(board) for _ in range(len(board))]
    arr[0][0] = 1
    q.append([0, 0, 0, 0, arr])
    q.append([0, 0, 1, 0, arr])
    answer = 600 * len(board) * len(board)
    while q:
        x, y, d, cost, arr = q.popleft()
        if cost >= answer:
            continue
        if x == len(board) - 1 and y == len(board) - 1:
            if cost < answer:
                answer = cost
            continue
        tmp = []
        for i in range(len(arr)):
            tmp.append(arr[i][:])
        cost += 100
            
        for i in range(4):
            if i == d:
                if 0 <= x + dx[i] < len(board) and 0 <= y + dy[i] < len(board) and board[x + dx[i]][y + dy[i]] == 0 and tmp[x + dx[i]][y + dy[i]] == 0:
                    tmp[x + dx[i]][y + dy[i]] = 1
                    q.appendleft([x + dx[i], y + dy[i], d, cost, tmp])
            else:
                if 0 <= x + dx[i] < len(board) and 0 <= y + dy[i] < len(board) and board[x + dx[i]][y + dy[i]] == 0 and tmp[x + dx[i]][y + dy[i]] == 0:
                    tmp[x + dx[i]][y + dy[i]] = 1
                    q.appendleft([x + dx[i], y + dy[i], i, cost + 500, tmp])
    
    return answer