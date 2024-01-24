N = 1000 - int(input())
count = 0
while N:
  count+=N//500
  N=N%500
  count+=N//100
  N=N%100
  count+=N//50
  N=N%50
  count+=N//10
  N=N%10
  count+=N//5
  N=N%5
  count+=N//1
  N=N%1

print(count)