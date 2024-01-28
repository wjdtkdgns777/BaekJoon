N,M = map(int,input().split())
J = int(input())
apple = [int(input()) for _ in range(J)]

min_cover = 1
max_cover = M
count = 0
for i in range(J):
  if apple[i]>max_cover:
    diff= abs(apple[i]-max_cover)
    count += diff
    max_cover += diff 
    min_cover += diff
      
  elif apple[i] < min_cover:
    diff= abs(min_cover-apple[i])
    count += diff
    min_cover -= diff  
    max_cover -= diff

print(count)