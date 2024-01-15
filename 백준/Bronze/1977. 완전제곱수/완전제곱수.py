M=int(input())
N=int(input())
list = [0]*10001
count2=[]

for i in range(101):
  list[i*i]=1
count =0
for i in range(M,N+1):
  if list[i]==1:
    count=count+i
    count2.append(i)

if(count>0):
  print(count)
  print(count2[0])

else:
  print(-1)