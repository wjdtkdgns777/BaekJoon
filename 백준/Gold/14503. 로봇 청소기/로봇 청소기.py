# 방 크기와 로봇 청소기의 초기 위치 및 방향 입력 받기
N, M = map(int, input().split())
r, c, d = map(int, input().split())

# 방의 상태 입력 받기 (0: 빈 칸, 1: 벽)
room = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 방향에 따른 이동 좌표 정의
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 청소한 칸의 수를 저장할 변수 초기화
cleaned = 0

# 왼쪽으로 회전하는 함수 정의
def turn_left(d):
    return (d - 1) % 4

# 청소기 작동 시작
while True:
    # 현재 위치가 청소되지 않았다면 청소하고, 청소한 칸 수 증가
    if room[r][c] == 0:
        room[r][c] = 2  # 청소한 위치는 2로 마킹
        cleaned += 1

    # 현재 위치에서 주변을 탐색하기 위한 변수
    turned = False
    for _ in range(4):
        d = turn_left(d)  # 왼쪽으로 회전
        nr, nc = r + directions[d][0], c + directions[d][1]
        
        # 청소하지 않은 빈 공간이 있다면 전진하고 다시 탐색 시작
        if room[nr][nc] == 0:
            r, c = nr, nc
            turned = True
            break

    # 4방향 모두 청소되었거나 벽인 경우
    if not turned:
        # 후진을 위한 위치 계산
        nr, nc = r - directions[d][0], c - directions[d][1]
        
        # 후진할 위치가 벽이라면 작동을 멈춤
        if room[nr][nc] == 1:
            break
        # 후진할 위치가 벽이 아니라면 후진
        r, c = nr, nc

# 청소한 칸의 수 출력
print(cleaned)
