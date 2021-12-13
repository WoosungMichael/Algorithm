import math
N = int(input())

for i in range(N):
    x = int(input())
    while True:
        if x < 3:
            print(2)
            break
        else:
            flag = False
            for j in range(2, int(math.sqrt(x))+1):
                if x % j == 0:
                    flag = True
                    break
            if flag:
                x += 1
            else:
                print(x)
                break
