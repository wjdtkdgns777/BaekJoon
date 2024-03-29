
(N, K) = map(int, input().split())
item = [[0, 0]]
dp = [[0] * (K + 1) for _ in range(N + 1)] 

for i in range(1, N + 1):
  item.append(list(map(int, input().split()))) 
  

for i in range(1, N + 1):
  for j in range(1, K + 1): 
    if j >= item[i][0]: 
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1]) 
    else: 
      dp[i][j] = dp[i-1][j] 
      

print(dp[N][K])