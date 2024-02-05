from collections import deque

queue = deque()
N,K = map(int,input().split())

queue.append(N)

def bfs(n,k):
  visited = [-1]*100001
  queue=deque([n])
  visited[n]=0
  while queue:
    x = queue.popleft()
    if x==k:
      return visited[x]

    for nx in (x-1,x+1,2*x):
      if 0<=nx <= 100000 and visited[nx] == -1:
        visited[nx]=visited[x]+1
        queue.append(nx)

print(bfs(N,K))