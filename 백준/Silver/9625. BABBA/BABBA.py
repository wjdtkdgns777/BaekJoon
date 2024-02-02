K = int(input())
dp = [[0,0] for _ in range(K+1)]

dp[0]=[1,0]

for i in range(1,K+1):
  dp[i][0] = dp[i-1][1]#a개수는 이전거 b개수랑 같음
  dp[i][1] = dp[i-1][1]+dp[i-1][0]

print(dp[K][0],dp[K][1])