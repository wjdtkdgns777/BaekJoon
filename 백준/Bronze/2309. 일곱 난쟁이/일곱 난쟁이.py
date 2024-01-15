from itertools import combinations

list = []
for _ in range (9):
  list.append(int(input()))

for i in combinations(list, 7):
  if sum(i) == 100:
    i=sorted(i)
    for height in i:
      print(height)
    break