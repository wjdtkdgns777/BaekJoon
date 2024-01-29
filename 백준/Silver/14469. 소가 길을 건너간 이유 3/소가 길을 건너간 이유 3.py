import sys

N = int(input())
cow = []
for _ in range(N):
  A,B=map(int,input().split())
  cow.append((A,B))
  
cow.sort(key=lambda x:x[0])
end_time = 0
for i in range(N):
  if(end_time>cow[i][0]):
    end_time =end_time+cow[i][1]
  else:
    end_time = cow[i][1]+cow[i][0]

print(end_time)