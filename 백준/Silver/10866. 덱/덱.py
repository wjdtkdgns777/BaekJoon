import sys
from collections import deque
deq = deque()
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
  command = sys.stdin.readline().split()
  if command[0]=='push_front':
    deq.appendleft(int(command[1]))
  elif command[0]=='push_back':
    deq.append(int(command[1]))
  elif command[0]=='pop_front':
    print(deq.popleft() if deq else -1)
  elif command[0]=='pop_back':
    print (deq.pop() if deq else -1)
  elif command[0]=='size':
    print(len(deq))
  elif command[0] == 'empty':
    print (0 if deq else 1)
  elif command[0] == 'front':
    print(deq[0] if deq else -1)
  elif command[0] == 'back':
    print(deq[-1] if deq else -1)
    