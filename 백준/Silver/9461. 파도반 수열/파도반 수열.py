T = int(input())
DP = [1,1,1,2,2,3,4,5,7,9]+[0]*100

for i in range(6,100):
  DP[i]=DP[i-1]+DP[i-5]

for _ in range(T):
  N = int(input())
  print(DP[N-1])