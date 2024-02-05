
cnt = 0
n = int(input())
s=[]
apt = []

dx = [0,0,-1,1]
dy=[1,-1,0,0]

for i in range(n):
  x = list(map(int,input()))
  s.append(x)

def dfs(x,y):
  global cnt
  cnt = cnt + 1
  s[x][y]=0
  for i in range(4):
    if(0<=x+dx[i]<n and 0<= y+dy[i]<n):
      if(s[x+dx[i]][y+dy[i]]==1):
        dfs(x+dx[i],y+dy[i])


for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            cnt= 0
            dfs(i,j)
            apt.append(cnt)


print(len(apt))
apt.sort()
for i in apt:
    print(i)