N,L = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
#L과 h[i]비교해서 낮으면 먹고 1길어기지

for i in range(len(h)):
  if L >= h[i]:
    L += 1
  else:
    break

print(L)