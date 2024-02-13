# n x n 크기의 보드에서 사탕의 색상을 입력받음
n = int(input())
board = [list(input()) for _ in range(n)]

# 보드에서 가장 긴 연속된 색상의 사탕의 개수를 확인하는 함수
def check(board):
    n = len(board)
    answer = 1
    for i in range(n):
        count = 1
        # 가로 방향으로 연속된 색상의 사탕 개수를 확인
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                count += 1
                answer = max(answer, count)
            else:
                count = 1
        # 세로 방향으로 연속된 색상의 사탕 개수를 확인
        count = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                count += 1
                answer = max(answer, count)
            else:
                count = 1
    return answer

# 최대 사탕 개수를 저장할 변수
answer = 0
# 보드의 모든 위치를 순회하면서 인접한 사탕을 교환
for i in range(n):
    for j in range(n):
        # 오른쪽 사탕과 교환 후 최대 연속 사탕 개수를 확인
        if j + 1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            temp = check(board)
            answer = max(answer, temp)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]  # 원상 복구
        # 아래쪽 사탕과 교환 후 최대 연속 사탕 개수를 확인
        if i + 1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            temp = check(board)
            answer = max(answer, temp)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 원상 복구

# 최대 사탕 개수 출력
print(answer)
