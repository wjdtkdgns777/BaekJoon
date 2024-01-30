import sys
from collections import deque

word = sys.stdin.readline().rstrip()
M = int(sys.stdin.readline())
word_front = deque(word)  # 커서 왼쪽의 모든 문자들
word_back = deque()  # 커서 오른쪽의 문자들은 초기에 비어 있음

for _ in range(M):
    instructor = sys.stdin.readline().rstrip().split()
    if instructor[0] == 'L' and word_front:
        word_back.appendleft(word_front.pop())
    elif instructor[0] == 'D' and word_back:
        word_front.append(word_back.popleft())
    elif instructor[0] == 'B' and word_front:
        word_front.pop()
    elif instructor[0] == 'P':
        word_front.append(instructor[1])

print(''.join(list(word_front) + list(word_back)))
