from itertools import combinations

N, M = map(int, input().split())
numbers = list(range(1, N+1))
combs = combinations(numbers, M)

for comb in combs:
    print(' '.join(map(str, comb)))
