import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x,y,h,w,earth,visited):
  visited[y][x]=True
  for i in range(8):
    nx,ny = x+dx[i],y+dy[i]
    if 0<=nx<w and 0<=ny<h and not visited[ny][nx] and earth[ny][nx]==1:
      dfs(nx,ny,h,w,earth,visited)


  

while True:
  w,h = map(int,input().split())
  if w==0 and h==0:
    break
  earth = [list(map(int,input().split())) for _ in range(h)]
  visited = [[False]*w for _ in range(h)]
  count = 0
  for i in range(h):
    for j in range(w):
      if earth[i][j]==1 and not visited[i][j]:
        count +=1
        dfs(j,i,h,w,earth,visited)
  print(count)
        
