N = int(input())
tester = list(map(int, input().split()))
B,C = map(int,input().split()) 
sum_teacher = 0+N


for i in range(N):
  tester2 = tester[i]-B
  if (tester2>0):
    if(tester2%C==0):
      sum_teacher += tester2//C
    else:
      sum_teacher += (tester2//C)+1

print(sum_teacher)