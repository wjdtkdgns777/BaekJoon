N = int(input())
P = [0] + list(map(int, input().split()))  # 1부터 인덱싱하기 위해 0을 앞에 추가
dp = [0] * (N + 1)  # DP 배열 초기화

# DP를 이용한 최댓값 계산
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + P[j])

# 결과 출력
print(dp[N])
