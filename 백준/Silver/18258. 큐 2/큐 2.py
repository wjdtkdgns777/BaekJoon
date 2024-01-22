import sys
from collections import deque

q = deque()

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(0 if q else 1)
    elif command[0] == 'front':
        print(q[0] if q else -1)
    elif command[0] == 'back':
        print(q[-1] if q else -1)
