N = input()
sum = sum(int(digit) for digit in N)

if '0' in N and sum %3 == 0:
  result = ''.join(sorted(N,reverse=True))
  print(result)

else:
  print(-1)