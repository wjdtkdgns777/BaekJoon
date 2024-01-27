X, Y = map(int,input().split())
count = 0
if (X >= Y):
  count = X + Y + Y//10
else:
  count = X + Y +X//10

print(count)