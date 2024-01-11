N = int(input())
max = 1
level = 1

while(N>max):
  max = max+6*level
  level = level+1

print(level)