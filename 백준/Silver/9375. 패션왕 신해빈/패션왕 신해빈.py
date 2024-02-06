T = int(input())
for _ in range(T):
  N = int(input())
  clothes = {}
  for _ in range(N):
    name,type = input().split()
    if type in clothes:
      clothes[type] += 1
    else:
      clothes[type] = 1

  result = 1
  for type in clothes:
    result *= (clothes[type] +1)

  print(result - 1)