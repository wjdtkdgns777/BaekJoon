def word_dp(N):
  dp = [0]*(N+1)
  dp[0]=1
  for n in range(1,N+1):
    for i in range(n):
      dp[n] += dp[i]*dp[n-i-1]
  return dp[N]
  
while(True):
  N = int(input())
  if N != 0:
    print(word_dp(N))
  else:
    exit(0)