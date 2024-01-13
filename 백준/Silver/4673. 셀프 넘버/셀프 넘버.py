constructor_number = [0]*10001

for i in range(1, 10001):
  sum_number = sum(map(int,str(i)))
  if (sum_number+i)<10001:
    constructor_number[sum_number+i] = 1

for i in range(1, 10001):
  if constructor_number[i]==0:
    print(i)