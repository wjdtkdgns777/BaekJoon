S = input()
list = []
for i in range(len(S)):
  list.append(''.join(S[i::]))
list.sort()

for s in list:
  print(s)