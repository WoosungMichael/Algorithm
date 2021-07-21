board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if "X" in board:
    print(-1)
else:
    print(board)

'''
board = input()

cnt = 0
answer = ""
for i in range(len(board)):
    if(board[i] == 'X'):
        cnt += 1
    else:
        while(cnt > 0):
            if(cnt >= 4):
                answer += "AAAA"
                cnt -= 4
            elif(cnt == 2):
                answer += "BB"
                cnt -= 2
            else:
                print(-1)
                exit()
        answer += "."

    if(i == len(board)-1):
        while(cnt > 0):
            if(cnt >= 4):
                answer += "AAAA"
                cnt -= 4
            elif(cnt == 2):
                answer += "BB"
                cnt -= 2
            else:
                print(-1)
                exit()

print(answer)
'''
