T = int(input())
for _ in range(T):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*(N+1) for _ in range(2)]

    # 첫 번째 열에 대한 초기화
    dp[0][1] = sticker[0][0]  # 첫 번째 행, 첫 번째 열
    dp[1][1] = sticker[1][0]  # 두 번째 행, 첫 번째 열

    # 점수 계산
    for i in range(2, N+1):
        dp[0][i] = max(dp[1][i-1] + sticker[0][i-1], dp[1][i-2] + sticker[0][i-1])
        dp[1][i] = max(dp[0][i-1] + sticker[1][i-1], dp[0][i-2] + sticker[1][i-1])

    # 최댓값 출력
    print(max(dp[0][N], dp[1][N]))
