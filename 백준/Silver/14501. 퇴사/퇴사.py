N = int(input())
date = []
dp = [0] * (N+1)

for _ in range(N):
  T,P = map(int,input().split())
  date.append((T,P))

for i in range(N-1,-1,-1):
  time = date[i][0]
  profit = date[i][1]

  if time + i <=N:
    dp[i] = max(profit+dp[i+time],dp[i+1])
  else:
    dp[i] = dp[i+1]

print(dp[0])