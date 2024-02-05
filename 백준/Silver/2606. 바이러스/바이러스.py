N = int(input())
S = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(S):
  A,B = map(int,input().split())
  graph[A].append(B)
  graph[B].append(A)

visited = [False]*(N+1)

def dfs(graph,start,visited):
  visited[start] = True
  for next in graph[start]:
    if not visited[next]:
      dfs(graph,next,visited)

dfs(graph,1,visited)

print(sum(visited)-1)