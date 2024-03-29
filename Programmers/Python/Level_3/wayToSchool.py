def solution(m, n, puddles):
    m, n = n, m
    arr = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        arr[i][0] = 1
    for i in range(m):
        arr[0][i] = 1
        
    p = [[0 for i in range(m)] for j in range(n)]
    for i in puddles:
        p[i[0] - 1][i[1] - 1] = 1
        arr[i[0] - 1][i[1] - 1] = 0
    
    for i in range(n):
        if p[i][0] == 1:
            for j in range(i, n):
                p[j][0] = 1
                arr[j][0] = 0
        
    for j in range(m):
        if p[0][j] == 1:
            for i in range(j, m):
                p[0][i] = 1
                arr[0][i] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            if p[i][j] == 0:
                arr[i][j] = (arr[i - 1][j] + arr[i][j - 1]) % 1000000007
                
    return arr[n - 1][m - 1] % 1000000007