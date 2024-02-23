N,M = map(int,input().split())
army = [list(input()) for _ in range(M)]
visited = [[False]*N for _ in range(M)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y,x,color):
  visited[y][x]=True
  count = 1
  for i in range(4):
    ny,nx = y+dy[i],x+dx[i]
    if 0<=ny<M and 0<=nx<N and not visited[ny][nx] and army[ny][nx]==color:
      count += dfs(ny,nx,color)
  return count


blue = 0
white = 0
for i in range(M):
  for j in range(N):
    if not visited[i][j] and army[i][j]=='B':
      blue+= dfs(i,j,army[i][j])**2
    elif not visited[i][j] and army[i][j]=='W':
      white+= dfs(i,j,army[i][j])**2

print(white,blue)