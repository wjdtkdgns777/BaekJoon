laser = input()
plate = 0
stack = []
for i in range(len(laser)):
  if laser[i] == '(':
    stack.append('(')
  else:
    if laser[i-1] == '(':
      stack.pop()
      plate += len(stack)
    else:
      stack.pop()
      plate+=1

print(plate)