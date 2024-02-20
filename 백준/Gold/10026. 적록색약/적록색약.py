import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(10**6)

N = int(input())
RGB = [input() for _ in range(N)]
RRB = [row.replace('G', 'R') for row in RGB]

# 전역 변수로 visited 배열 선언
visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, board):
    global visited  # 전역 변수 사용 선언
    visited[x][y] = True
    current_color = board[x][y]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == current_color:
            dfs(nx, ny, board)

def count_areas(board):
    global visited  # 전역 변수 사용 선언
    visited = [[False]*N for _ in range(N)]  # 방문 배열 초기화
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, board)
                count += 1
    return count

print(count_areas(RGB), count_areas(RRB))
