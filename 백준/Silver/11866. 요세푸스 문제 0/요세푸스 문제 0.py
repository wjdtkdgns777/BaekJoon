from collections import deque
N,K = map(int,input().split())
list = []
q = deque(range(1,N+1))
while q:
  q.rotate(-K+1)
  list.append(q.popleft())

print("<" + ", ".join(map(str,list))+">")