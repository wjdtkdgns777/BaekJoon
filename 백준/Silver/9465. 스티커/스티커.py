T = int(input())
for _ in range(T):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    # 첫 번째 열에 대한 초기화
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if N > 1:
        dp[0][1] = sticker[1][0] + sticker[0][1]
        dp[1][1] = sticker[0][0] + sticker[1][1]

    # 점수 계산 로직
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[1][i-2], dp[0][i-2]) + sticker[1][i]

    # 최댓값 출력
    if N > 0:
        print(max(dp[0][N-1], dp[1][N-1]))
