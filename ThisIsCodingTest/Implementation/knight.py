position = input()

c = position[0]
r = position[1]

if 'c' <= c and c <= 'f':
    if '3' <= r and r <= '6':
        answer = 8
    elif r == '2' or r == '7':
        answer = 6
    else:
        answer = 4
elif c == 'b' or c == 'g':
    if '3' <= r and r <= '6':
        answer = 6
    elif r == '2' or r == '7':
        answer = 4
    else:
        answer = 3
else:
    if '3' <= r and r <= '6':
        answer = 4
    elif r == '2' or r == '7':
        answer = 3
    else:
        answer = 2

print(answer)