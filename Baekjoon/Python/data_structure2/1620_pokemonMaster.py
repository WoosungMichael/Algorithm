N, M = map(int, input().split())

pokemon = {}
num = {}
index = 1
for i in range(N):
    monster = input()
    pokemon[index] = monster
    num[monster] = index
    index += 1

for i in range(M):
    Q = input()
    if 49 <= ord(Q[0]) <= 57:
        print(pokemon[int(Q)])
    else:
        print(num[Q])
