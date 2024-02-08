from collections import deque
def solution(s):
    answer = True
    queue = deque()
    for i in range(len(s)):
        if not queue and s[i] == ')':
            return False
        elif queue and queue[-1]=='(' and s[i] == ')':
            queue.pop()
        else:
            queue.append(s[i])
    if queue:
        return False

    return True