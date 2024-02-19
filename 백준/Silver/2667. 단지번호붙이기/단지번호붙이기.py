n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 상하좌우 이동을 위한 방향 벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    # 상하좌우 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 지도 범위 내에서
        if 0 <= nx < n and 0 <= ny < n:
            # 연결된 집이 있고 아직 방문하지 않았다면
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

print(len(result))
for r in sorted(result):
    print(r)
