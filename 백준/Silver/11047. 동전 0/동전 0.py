N,K = map(int,input().split())
coin = []

for _ in range(N):
  coin.append(int(input()))
count = 0
for i in range(N-1,-1,-1):
  count = count+ K//coin[i]
  K = K%coin[i]

print(count)