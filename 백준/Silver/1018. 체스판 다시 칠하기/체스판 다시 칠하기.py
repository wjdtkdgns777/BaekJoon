N, M = map(int, input().split())
board = [input() for _ in range(N)]

def count_recolor(start_row, start_col, color):
    count = 0
    for i in range(start_row, start_row + 8):
        for j in range(start_col, start_col + 8):
            if ((i + j) % 2 == 0 and board[i][j] != color) or \
               ((i + j) % 2 != 0 and board[i][j] == color):
                count += 1
    return count

min_recolor = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        recolor_w = count_recolor(i, j, 'W')
        recolor_b = count_recolor(i, j, 'B')
        min_recolor = min(min_recolor, recolor_w, recolor_b)

print(min_recolor)