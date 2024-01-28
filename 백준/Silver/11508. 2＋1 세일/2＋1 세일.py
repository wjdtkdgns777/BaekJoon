N = int(input())
tree = [int(input()) for _ in range(N)]
tree.sort(reverse=True)
sum = 0
for i in range(N):
  if((i+1)%3==0):
    continue
  else:
    sum += tree[i]

print(sum)