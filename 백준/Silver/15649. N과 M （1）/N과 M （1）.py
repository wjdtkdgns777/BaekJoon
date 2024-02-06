from itertools import permutations

N,M = map(int,input().split())
numbers = list(range(1,N+1))
per = permutations(numbers,M)

for i in per:
  print(' '.join(map(str,i)))