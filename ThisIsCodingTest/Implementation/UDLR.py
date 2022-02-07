N = int(input())
action = list(input().split())

UD = 1
LR = 1

for i in action:
    if i == "U" and UD > 1:
        UD -= 1
    elif i == "D" and UD < N:
        UD += 1
    elif i == "L" and LR > 1:
        LR -= 1
    elif i == "R" and LR < N:
        LR += 1

print(UD, LR)