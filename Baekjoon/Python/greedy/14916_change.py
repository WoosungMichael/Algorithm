change = int(input())

cnt = 0
while(change % 5 != 0 and change > 0):
    change -= 2
    cnt += 1

if(change < 0):
    print(-1)
else:
    print(cnt+change//5)

'''

if(change == 1 or change == 3):
    cnt = -1
else:
    if(change % 10 == 0):
        cnt = change//5
    elif(change % 10 == 1):
        cnt = (change-6)//5 + 3
    elif(change % 10 == 2):
        cnt = (change-2)//5 + 1
    elif(change % 10 == 3):
        cnt = (change-8)//5 + 4
    elif(change % 10 == 4):
        cnt = (change-4)//5 + 2
    elif(change % 10 == 5):
        cnt = change//5
    elif(change % 10 == 6):
        cnt = (change-6)//5 + 3
    elif(change % 10 == 7):
        cnt = (change-2)//5 + 1
    elif(change % 10 == 8):
        cnt = (change-8)//5 + 4
    elif(change % 10 == 9):
        cnt = (change-4)//5 + 2

print(cnt)
'''
