from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def bfs(height, x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))

def find_max_safe_area():
    max_area = 0
    for height in range(max(map(max, grid))):  
        visited = [[False] * N for _ in range(N)]
        safe_area = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] > height and not visited[i][j]:
                    bfs(height, i, j, visited)
                    safe_area += 1
        max_area = max(max_area, safe_area)
    return max_area

print(find_max_safe_area())
