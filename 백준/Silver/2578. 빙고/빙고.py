def count_bingo_lines(board):
    bingo_lines = 0

    # 가로 체크
    for row in board:
        if sum(row) == 0:
            bingo_lines += 1

    # 세로 체크
    for col in range(5):
        if sum(board[row][col] for row in range(5)) == 0:
            bingo_lines += 1

    # 대각선 체크
    if sum(board[i][i] for i in range(5)) == 0:
        bingo_lines += 1
    if sum(board[i][4 - i] for i in range(5)) == 0:
        bingo_lines += 1

    return bingo_lines

# 빙고판 입력
bingo_board = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부르는 숫자 입력
called_numbers = []
for _ in range(5):
    called_numbers += list(map(int, input().split()))

# 숫자를 부를 때마다 빙고판 갱신 및 빙고 체크
for called_count, number in enumerate(called_numbers):
    for row in range(5):
        for col in range(5):
            if bingo_board[row][col] == number:
                bingo_board[row][col] = 0  # 해당 숫자를 지움

    # 빙고를 세 개 이상 만들었는지 확인
    if called_count >= 11:  # 최소 12개의 숫자가 불려야 3빙고 가능
        bingo_lines = count_bingo_lines(bingo_board)
        if bingo_lines >= 3:
            print(called_count + 1)  # 0-based index이므로 +1
            break
