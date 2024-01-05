N,M = map(int,input().split())

baskets = [0]*(N+1)
for q in range(1,N+1):
  baskets[q]=q

for _ in range(M):
  i,j = map(int,input().split())
  baskets[i],baskets[j] = baskets[j],baskets[i]


for i in range(1,N+1):
  print(baskets[i],end=' ')