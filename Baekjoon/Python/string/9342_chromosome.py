T = int(input())

s_list = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(T):
    str = input()
    flag1 = True
    flag2 = False
    flag3 = False
    flag4 = False
    if str[0] not in s_list:
        print("Good")
    index = 1
    while(index < len(str) and str[index] == 'A'):
        index += 1
    while(index < len(str) and str[index] == 'F'):
        index += 1
    while(index < len(str) and str[index] == 'C'):
        index += 1
    if index < len(str) and str[index] not in s_list:
        print("Good")
    if index + 1 != len(str) - 1:
        print("Good")
    print("Infected!")
