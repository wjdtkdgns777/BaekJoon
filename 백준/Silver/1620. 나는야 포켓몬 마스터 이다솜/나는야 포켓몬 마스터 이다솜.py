import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_by_name = {}
pokemon_by_number = {}

for i in range(1, N + 1):
    pokemon_name = sys.stdin.readline().strip()  # 개행 문자 제거
    pokemon_by_name[pokemon_name] = i
    pokemon_by_number[i] = pokemon_name

for _ in range(M):
    quiz = sys.stdin.readline().strip()  # 개행 문자 제거
    if quiz.isdigit():
        print(pokemon_by_number[int(quiz)])
    else:
        print(pokemon_by_name[quiz])
