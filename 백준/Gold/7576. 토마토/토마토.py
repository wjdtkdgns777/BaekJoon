from collections import deque
M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
queue = deque([])
for i in range(N):
  for j in range(M):
    if tomato[i][j]==1:
      queue.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
  while queue:
    y,x = queue.popleft()
    for i in range(4):
      nx,ny = x+dx[i],y+dy[i]
      if 0<=nx<M and 0<=ny<N and tomato[ny][nx]==0:
        tomato[ny][nx] = tomato[y][x]+1
        queue.append((ny,nx))
bfs()

max_days = 0
for row in tomato:
  for t in row:
    if t==0:
      print(-1)
      exit(0)
    max_days=max(max_days,t)

print(max(max_days-1,0))