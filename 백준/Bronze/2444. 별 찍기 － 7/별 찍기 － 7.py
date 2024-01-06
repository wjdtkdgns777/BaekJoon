N = int(input())

# 위쪽 삼각형 부분
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

# 아래쪽 삼각형 부분 (가장 긴 행을 제외하고)
for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
