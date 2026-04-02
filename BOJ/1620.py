N, M = map(int, input().split())

pokemon_list = ['']
pokemon_dict = {}

for i in range(1, N + 1):
    name = input().strip()
    pokemon_list.append(name)
    pokemon_dict[name] = i

for _ in range(M):
    pass