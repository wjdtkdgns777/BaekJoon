from itertools import combinations

N,S = map(int,input().split())
number = list(map(int,input().split()))
count = 0

for i in range(1,N+1):
  for combo in combinations(number, i):
    if sum(combo) == S:
      count +=1

print(count)