import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
q = deque()
for _ in range(N):
    commands = sys.stdin.readline().rstrip().split()
    command = commands[0]

    if command == '1':
        q.appendleft(commands[1])
    elif command == '2':
        q.append(commands[1])
    elif command == '3':
        print(q.popleft() if len(q) > 0 else -1)
    elif command == '4':
        print(q.pop() if len(q) > 0 else -1)
    elif command == '5':
        print(len(q))
    elif command == '6':
        print(0 if len(q) > 0 else 1)
    elif command == '7':
        print(q[0] if len(q) > 0 else -1)
    elif command == '8':
        print(q[-1] if len(q) > 0 else -1)
