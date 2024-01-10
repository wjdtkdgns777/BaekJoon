tile = [[0]*100 for _ in range(100)]
sum =0
N = int(input())
for _ in range(N):
  x,y = map(int,input().split())
  for i in range(x,x+10):
    for j in range (y,y+10):
      if (i<100 and j<100):
        tile[i][j] = 1

for i in range(100):
  for j in range(100):
    if(tile[i][j]==1):
      sum=sum+1

print(sum)