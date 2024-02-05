import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

def dfs(y, x):
    # 범위를 벗어났거나, 배추가 없거나, 이미 방문한 경우 리턴
    if y < 0 or y >= n or x < 0 or x >= m or graph[y][x] == 0 or visited[y][x]:
        return
    visited[y][x] = True  # 현재 위치 방문 처리
    # 상하좌우 탐색
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)

T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    m, n, k = map(int, input().split())  # m: 가로 길이, n: 세로 길이, k: 배추 위치 개수
    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1  # 배추 위치에 1 표시

    count = 0  # 필요한 배추흰지렁이 수
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:  # 배추가 있고 아직 방문하지 않은 경우
                dfs(i, j)  # DFS 수행
                count += 1  # 새로운 단지 발견, 지렁이 수 증가
    print(count)  # 결과 출력
