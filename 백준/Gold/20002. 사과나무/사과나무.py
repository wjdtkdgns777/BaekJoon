def max_profit(N, profits):
    # Step 1: 누적 합 배열 생성
    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = profits[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
    
    max_profit_value = float('-inf')

    # Step 2: 모든 K x K 부분 행렬의 합 계산
    for k in range(1, N + 1):
        for i in range(k, N + 1):
            for j in range(k, N + 1):
                total_profit = (prefix_sum[i][j]
                               - prefix_sum[i-k][j]
                               - prefix_sum[i][j-k]
                               + prefix_sum[i-k][j-k])
                max_profit_value = max(max_profit_value, total_profit)

    return max_profit_value

# 입력 받기
N = int(input().strip())
profits = [list(map(int, input().strip().split())) for _ in range(N)]

# 최대 이익 계산 및 출력
result = max_profit(N, profits)
print(result)