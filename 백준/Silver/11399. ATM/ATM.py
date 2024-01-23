N = int(input())
list = list(map(int,input().split()))

list.sort()
sum = 0 
for i in range(N):
  sum = sum + list[i]*(N-i)

print(sum)