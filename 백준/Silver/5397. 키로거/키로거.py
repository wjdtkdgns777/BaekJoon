from collections import deque

T = int(input())
for _ in range(T):
    password = input()
    left_deque = deque()
    right_deque = deque()
    for i in range(len(password)):
        if password[i] == '-':
            if left_deque:
                left_deque.pop()
        elif password[i] == '<':
            if left_deque:
                right_deque.appendleft(left_deque.pop())
        elif password[i] == '>':
            if right_deque:
                left_deque.append(right_deque.popleft())
        else:
            left_deque.append(password[i])
    print(''.join(left_deque) + ''.join(right_deque))
