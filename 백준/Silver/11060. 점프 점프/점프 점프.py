N = int(input())
jump = list(map(int,input().split()))
DP=[1e9]*(N+1)
DP[1]=0

for i in range(1,N+1):
  for j in range(1,i):
    if (j+jump[j-1]>=i):
      DP[i] = min(DP[i],DP[j]+1)

print(DP[N] if DP[N]!=1e9 else -1)