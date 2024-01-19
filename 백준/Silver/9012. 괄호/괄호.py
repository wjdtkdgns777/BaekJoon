T = int(input())

for _ in range (T):
  ps = input()
  stack = []
  is_valid = True
  
  for ch in ps:
    if ch == '(':
      stack.append(ch)
    else:
      if not stack:
        is_valid = False
        break
      stack.pop()

  if stack or not is_valid:
    print("NO")
  else:
    print("YES")
