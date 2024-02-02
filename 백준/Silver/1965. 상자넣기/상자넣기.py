N = int(input())
box = list(map(int,input().split()))
#i,j로 돌면서 max(박스+1)
dp = [0]*(N+1)


for i in range(N):
  for j in range(i):
    if(box[i]>box[j]):
      dp[i]=max(dp[i],dp[j]+1)

print(max(dp)+1)