A = int(input())
T = int(input())
x = int(input())

total = 0
cnt = [0, 0]
arr = []
turn = 2

while(True):
    for i in range(2):

        cnt[0] += 1
        if(x == 0):
            if(cnt[0] == T):
                print(total % A)
                exit()
        total += 1
        cnt[1] += 1
        if(x == 1):
            if(cnt[1] == T):
                print(total % A)
                exit()
        total += 1

    for i in range(turn):
        cnt[0] += 1
        if(x == 0):
            if(cnt[0] == T):
                print(total % A)
                exit()
        total += 1

    for i in range(turn):
        cnt[1] += 1
        if(x == 1):
            if(cnt[1] == T):
                print(total % A)
                exit()
        total += 1

    turn += 1
