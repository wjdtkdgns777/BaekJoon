N = int(input())
case = [0]*1000001
case[1] = 1
#1
case[2] = 2
#11 or 00
case[3] = 3
#111 100 001
case[4] = 5
#1111 0000 1100 1001 0011
for i in range(3, N+1):
  case[i] = (case[i-2]+case[i-1])%15746

print(case[N])


