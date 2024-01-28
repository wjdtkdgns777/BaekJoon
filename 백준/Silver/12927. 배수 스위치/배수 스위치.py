N = input()
bulbs = list(N)
count = 0
for i in range(len(bulbs)):
  if bulbs[i]=='Y':
    count +=1
    for j in range(i,len(bulbs),i+1):
        if bulbs[j] == 'Y':
          bulbs[j] = 'N'
        elif bulbs[j] == 'N':
          bulbs[j] = 'Y'

print(count if 'Y' not in bulbs else -1)