import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = []
pokemon_dict = {}

for i in range(N):
    monster = input().rstrip()
    pokemon.append(monster)
    pokemon_dict[monster] = i + 1

for i in range(M):
    Q = input().rstrip()
    if 49 <= ord(Q[0]) <= 57:
        print(pokemon[int(Q)-1])
    else:
        print(pokemon_dict[Q])
