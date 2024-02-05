import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 그래프 구성
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    visited[start] = True
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(next_node)

# 연결 요소의 개수를 세는 변수
count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)