N,K = map(int,input().split())
sum = 0
for i in range(K):
  sum += i+1
#(N - sum) % K == K-1 아니면 K개
if sum>N:
  print(-1)
else:
  if(N-sum)%K==0:
    print(K-1)
  else:
    print(K)