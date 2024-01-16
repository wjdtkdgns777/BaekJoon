N,M =map(int,input().split())
list = []*N

for i in range(1,N+1):
  if(N%i==0):
    list.append(i)

if(len(list)<M):
  print(0)
else:
  print(list[M-1])