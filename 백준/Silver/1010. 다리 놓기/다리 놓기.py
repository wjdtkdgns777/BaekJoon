import math

def count_bridges(n,m):
  return math.comb(m,n)

T = int(input())
for _ in range(T):
  N,M = map(int,input().split())
  print(count_bridges(N,M))