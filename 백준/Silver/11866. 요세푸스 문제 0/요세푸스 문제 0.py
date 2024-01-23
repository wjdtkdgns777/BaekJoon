from collections import deque

N,K = map(int,input().split())
first_que = deque()
ans_que = deque()

for i in range(1,N+1):
  first_que.append(i)

while first_que:
  for i in range(K-1):
    first_que.append(first_que.popleft())
  ans_que.append(first_que.popleft())

print("<", ", ".join(map(str, ans_que)), ">", sep="")