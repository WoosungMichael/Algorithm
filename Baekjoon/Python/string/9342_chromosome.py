T = int(input())

s_list = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(T):
    str = input()
    if str[0] not in s_list:
        print("Good")
        continue
    index = 1
    while(index < len(str) and str[index] == 'A'):
        index += 1
    while(index < len(str) and str[index] == 'F'):
        index += 1
    while(index < len(str) and str[index] == 'C'):
        index += 1
    if index < len(str) and str[index] not in s_list:
        print("Good")
        continue
    if index != len(str):
        print("Good")
        continue
    print("Infected!")
