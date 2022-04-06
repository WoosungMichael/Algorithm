N = int(input())

like = []
like_dic = {}
for i in range(N ** 2):
    tmp = list(map(int, input().split()))
    like.append(tmp)
    like_dic[tmp[0]] = [tmp[1], tmp[2], tmp[3], tmp[4]]
    
arr = [[0] * N for i in range(N)]

answer = 0
x, y = -1, -1
for i in range(N ** 2):
    max_cnt = -1
    max_blank = -1
    for j in range(N):
        for k in range(N):
            cnt = 0
            blank = 0
            if arr[j][k] == 0:
                if j > 0 and arr[j - 1][k] in like[i][1:]:
                    cnt += 1
                if j > 0 and arr[j - 1][k] == 0:
                    blank += 1

                if k > 0 and arr[j][k - 1] in like[i][1:]:
                    cnt += 1
                if k > 0 and arr[j][k - 1] == 0:
                    blank += 1

                if j < N - 1 and arr[j + 1][k] in like[i][1:]:
                    cnt += 1
                if j < N - 1 and arr[j + 1][k] == 0:
                    blank += 1

                if k < N - 1 and arr[j][k + 1] in like[i][1:]:
                    cnt += 1
                if k < N - 1 and arr[j][k + 1] == 0:
                    blank += 1

            if cnt > max_cnt:
                max_cnt = cnt
                max_blank = blank
                x, y = j, k
            elif cnt == max_cnt:
                if blank > max_blank:
                    max_blank = blank
                    x, y = j, k
    arr[x][y] = like[i][0]

for i in range(N):
    for j in range(N):
        cnt = 0
        if i > 0 and arr[i - 1][j] in like_dic[arr[i][j]]:
            cnt += 1
        if j > 0 and arr[i][j - 1] in like_dic[arr[i][j]]:
            cnt += 1
        if i < N - 1 and arr[i + 1][j] in like_dic[arr[i][j]]:
            cnt += 1
        if j < N - 1 and arr[i][j + 1] in like_dic[arr[i][j]]:
            cnt += 1

        if cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        elif cnt == 4:
            answer += 1000

print(answer)