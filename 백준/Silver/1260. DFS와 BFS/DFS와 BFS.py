from collections import deque

N, M, V = map(int, input().split())  # 입력 받기
graph = [[] for _ in range(N + 1)]  # 그래프를 인접 리스트로 표현
visited = [False] * (N + 1)  # 방문 처리 배열

for _ in range(M):  # 간선 정보 입력 받아 그래프 구성
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)  # 무방향 그래프이므로 양방향 처리

# DFS 함수
def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드 방문 처리
    print(v, end=' ')  # 현재 노드 출력
    for i in sorted(graph[v]):  # 인접한 노드들을 정렬하여 순회
        if not visited[i]:  # 방문하지 않은 노드라면
            dfs(graph, i, visited)  # 재귀적으로 DFS 수행

#graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

# BFS 함수
def bfs(graph, start):
    visited = [False] * (len(graph) + 1)  # 방문 처리를 위한 배열
    queue = deque([start])  # 시작 노드를 큐에 삽입
    visited[start] = True  # 시작 노드 방문 처리
    while queue:
        v = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력
        print(v, end=' ')
        for i in sorted(graph[v]):  # 인접한 노드들을 정렬하여 순회
            if not visited[i]:
                queue.append(i)  # 방문하지 않은 노드를 큐에 삽입
                visited[i] = True  # 방문 처리





dfs(graph, V, visited)  # DFS 수행
print()
bfs(graph, V)  # BFS 수행
