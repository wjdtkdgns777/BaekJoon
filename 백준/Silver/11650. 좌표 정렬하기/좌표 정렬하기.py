import sys

N = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(N):
  x,y = map(int,sys.stdin.readline().split())
  numbers.append((x,y))

numbers.sort(key=lambda x:(x[0],x[1]))

for i in range(N):
  print(numbers[i][0],numbers[i][1])