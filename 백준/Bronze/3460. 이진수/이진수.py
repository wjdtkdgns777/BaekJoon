T = int(input())
for _ in range(T):
  num = int(input())
  results = []
  position = 0
  while num>0:
    if num % 2 ==1:
      results.append(str(position))
    num //=2
    position += 1
  print(' '.join(results))